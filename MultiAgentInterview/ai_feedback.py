def evaluate_answer(question, answer):

    answer = answer.strip()

    if len(answer) < 20:
        return {
            "technical": 5,
            "communication": 6,
            "overall": "Your answer is too short. Please explain in more detail."
        }

    elif len(answer) < 60:
        return {
            "technical": 7,
            "communication": 7,
            "overall": "Good answer, but more examples and technical details would improve it."
        }

    else:
        return {
            "technical": 9,
            "communication": 9,
            "overall": "Excellent answer with clear explanation and sufficient technical detail."
        }