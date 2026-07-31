from agents.hr_agent import HRAgent
from agents.technical_agent import TechnicalAgent
from agents.coding_agent import CodingAgent


class Manager:

    def __init__(self):
        self.hr = HRAgent()
        self.tech = TechnicalAgent()
        self.code = CodingAgent()

    def get_all_questions(self):

        all_questions = []

        for q in self.hr.get_questions():
            q["agent"] = "HR"
            all_questions.append(q)

        for q in self.tech.get_questions():
            q["agent"] = "Technical"
            all_questions.append(q)

        for q in self.code.get_questions():
            q["agent"] = "Coding"
            all_questions.append(q)

        
        return all_questions
    
