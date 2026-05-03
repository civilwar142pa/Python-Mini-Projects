class Question:
    def __init__(self, type, text, correct_answer, all_answers):
        self.type = type
        self.text = text
        self.answer = correct_answer
        self.all_answers = all_answers