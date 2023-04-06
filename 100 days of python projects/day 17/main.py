from data import question_data
from question_module import Question
from random import choice
from quiz_brain import QuizBrain

question_bank = []
for question in range(len(question_data)):
    new_question =  Question(question_data[question]["question"], question_data[question]["correct_answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()

    

