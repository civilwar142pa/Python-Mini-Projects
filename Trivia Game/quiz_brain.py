#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print("="*50)
        print(f"Q.{self.question_number}: {current_question.text}: ")
        if current_question.type == "multiple":
            print(f"{current_question.all_answers}")
        else:
            print("(True/False)")
        user_answer = input("Answer: ")
        self.check_answer(user_answer, current_question.answer)
      
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}") 
        
        if self.question_number < len(self.question_list):
            print(f"Your current scores is: {self.score}/{self.question_number}")