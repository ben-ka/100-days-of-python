from question_module import Question
from random import choice
class QuizBrain:
    def __init__(self,questions_list) :
        self.question_num = 0
        self.question_list = questions_list
        self.score = 0

    def check_answer(self,guess,correct):
        if correct =="True" :
            if guess.startswith("t"):
                return True
            else:
                return False
        else:
            if guess.startswith("f"):
                return True
            else:
                return False

    def next_question(self):
        while self.question_num < len(self.question_list):
            current_q = choice(self.question_list)
            guess = input(f"q.{self.question_num+1}:  {current_q.text} true/false: ").lower()
            is_correct = self.check_answer(guess,current_q.answer)
            
            if is_correct ==False:
                print("you're wrong")
                print(f"the correct answer is {current_q.answer}")
            else:
                print("well done. you're right")
                print(f"the correct answer is {current_q.answer}")
                
                self.score +=1
            print(f"your current score is: {self.score}/{self.question_num+1}")
            self.question_num +=1 
            print("\n")   
               

        print(f"congratulations. you have completed the quiz. your final score is: {(self.score/self.question_num)* 100}%")  

   