import random 
import json

class Question:
    def __init__(self, question:str, correct_answer:str, incorrect_answers:list,category:str, difficulty:str):
        if difficulty not in ('easy', 'medium', 'hard'):
            raise AttributeError
        self.difficulty = difficulty
        self.question = question
        incorrect_answers.append(correct_answer)
        random.shuffle(incorrect_answers)
        self.answers = incorrect_answers
        self.category = category
        self.answer_id = self.answers.index(correct_answer) + 1

    def __str__(self):
        numbered_answers = [self.question]
        for position, answer in enumerate(self.answers):
            numbered_answers.append(f'{position+1} {answer}')
        return ' \n'.join(numbered_answers)
        
        
        
            
            

             
        


Question("What year was Queen Elizabeth II born?", "1926", ["1923","1929","1930"],"General Knowledge", "hard").__str__()
    