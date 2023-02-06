import json
from question import Question
import random


class QuestionLibrary:
    def __init__(self, filename='trivia.json'):
        self.questions = []
        with open(filename, 'r') as f:
            data = json.load(f)
        for item in data:
            self.questions.append(Question(item['question'], item['correct_answer'],
                                 item['incorrect_answers'], item['category'], item['difficulty']))
          
    def __len__(self):
        return len(self.questions)
    
    def get_categories(self):
        category_set = set([])
        for question in self.questions:
            category_set.add(question.category.lower())
        return list(category_set)

    def get_questions(self, category: str = None, difficulty: str = None, number: int = 0):
        question_list = []
        random.shuffle(self.questions)
        
        if (number <= 0) or (number >= len(self.questions)):
            number = 0
            for question in self.questions:
                if (category in self.get_categories()) and (difficulty in ('easy', 'medium', 'hard')):
                    if (question.category.lower() == category) and (question.difficulty.lower() == difficulty):
                        number += 1
                elif (category in self.get_categories()) or (difficulty in ('easy', 'medium', 'hard')):
                    if (question.category.lower() == category):
                        number += 1
                    elif (question.difficulty.lower() == difficulty):
                        number += 1
                else:
                    number = len(self.questions)
                    
        for question in self.questions:
            if (category in self.get_categories()) and (difficulty in ('easy', 'medium', 'hard')):
                if (question.category.lower() == category) and (question.difficulty.lower() == difficulty):
                    question_list.append(question)
            elif (category in self.get_categories()) or (difficulty in ('easy', 'medium', 'hard')):
                if question.category.lower() == category:
                    question_list.append(question)
                elif question.difficulty.lower() == difficulty:
                    question_list.append(question)
            else:
                question_list.append(question)
                
            if len(question_list) == number:
                return question_list

for item in QuestionLibrary().get_questions('animals', '', 5):
    print(item.difficulty, item.category)


