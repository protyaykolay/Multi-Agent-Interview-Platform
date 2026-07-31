from flask import Flask, render_template, request, redirect, session
from agents.manager import Manager
from ai_feedback import evaluate_answer
from database.save_result import save_result

# ------------------------------------
# Flask App
# ------------------------------------
app = Flask(__name__)
app.secret_key = "brainware123"

# ------------------------------------
# Load Questions
# ------------------------------------
manager = Manager()
questions = manager.get_all_questions()

# ------------------------------------
# Home Page
# ------------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ------------------------------------
# Candidate Login
# ------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        session["name"] = request.form["name"]
        session["email"] = request.form["email"]
        session["student_id"] = request.form["student_id"]

        session["current_question"] = 0
        session["score"] = 0
        session["ai_reports"] = []

        return redirect("/interview")

    return render_template("login.html")

# ------------------------------------
# Interview Page
# ------------------------------------
@app.route("/interview", methods=["GET", "POST"])
def interview():

    if "name" not in session:
        return redirect("/login")

    current_question = session.get("current_question", 0)
    score = session.get("score", 0)
    ai_reports = session.get("ai_reports", [])

    # --------------------------------
    # Process Answer
    # --------------------------------
    if request.method == "POST":

        user_answer = request.form["answer"]

        question_text = questions[current_question]["question"]
        correct_answer = questions[current_question]["answer"]

        report = evaluate_answer(question_text, user_answer)

        ai_reports.append({
            "question": question_text,
            "technical": report["technical"],
            "communication": report["communication"],
            "overall": report["overall"]
        })

        if correct_answer != "":
            if user_answer.strip().lower() == correct_answer.strip().lower():
                score += 1

        current_question += 1

        session["current_question"] = current_question
        session["score"] = score
        session["ai_reports"] = ai_reports

    # ------------------------------------
    # Interview Finished
    # ------------------------------------
    if current_question >= len(questions):

        final_score = score

        tech_total = 0
        comm_total = 0

        for report in ai_reports:
            tech_total += report["technical"]
            comm_total += report["communication"]

        avg_tech = round(tech_total / len(ai_reports), 1)
        avg_comm = round(comm_total / len(ai_reports), 1)

        save_result(
            session["name"],
            session["email"],
            session["student_id"],
            final_score
        )

        name = session["name"]
        reports = ai_reports

        session.pop("current_question", None)
        session.pop("score", None)
        session.pop("ai_reports", None)

        technical_scores = []
        communication_scores = []
        question_names = []

        for r in reports:
            technical_scores.append(r["technical"])
            communication_scores.append(r["communication"])
            question_names.append(r["question"])

        return render_template(
            "result.html",
            score=final_score,
            name=name,
            tech=avg_tech,
            communication=avg_comm,
            reports=reports,
            technical_scores=technical_scores,
            communication_scores=communication_scores,
            question_names=question_names
        )

    # ------------------------------------
    # Show Current Question
    # ------------------------------------
    return render_template(
        "interview.html",
        question=questions[current_question],
        current=current_question + 1,
        total=len(questions)
    )

# ------------------------------------
# Logout
# ------------------------------------
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

# ------------------------------------
# Run Application
# ------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
