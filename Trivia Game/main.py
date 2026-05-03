from data import question_data as qd
from question_model import Question
from quiz_brain import QuizBrain
import random
import html

def question_sort(question_bank):
    choice = input("Which category would you like? (history, science, books, video games, music, movies or all) ").lower()
    random.shuffle(qd)
    
    categories = {
        "history": "History",
        "science": "Science &amp; Nature",
        "books": "Entertainment: Books",
        "video games": "Entertainment: Video Games",
        "music": "Entertainment: Music",
        "movies": "Entertainment: Film"
    }
    
    for entry in qd:
        if len(question_bank) >= 10:
            break
        
        if choice == "all" or entry["category"] == categories.get(choice):
            organize_question(question_bank, entry)
            
    return question_bank
    

def organize_question(question_bank, entry):
    type = entry["type"]
    text = html.unescape(entry["question"]) #cleans weirdo characters from the question
    all_answers = entry["incorrect_answers"] + [entry["correct_answer"]]
    random.shuffle(all_answers)
    correct_answer = entry["correct_answer"]
    new_question = Question(type, text, correct_answer, all_answers)
    question_bank.append(new_question)

question_bank = []
question_bank = question_sort(question_bank)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): 
    quiz.next_question()
    
print("="*50)
print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")