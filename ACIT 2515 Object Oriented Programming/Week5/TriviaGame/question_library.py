import json
from question import Question
import random


class QuestionLibrary:
    def __init__(self, filename: str ='trivia.json'):
        """The constructor for the QuestionLibrary class.
        
        Args:
        filename (str): the name of the JSON file to load the questions from (default: 'trivia.json')
        """
        self.questions = []
        with open(filename, 'r') as f:
            data = json.load(f)
        for item in data:
            self.questions.append(Question(item['question'], item['correct_answer'],
                                 item['incorrect_answers'], item['category'], item['difficulty']))
          
    def __len__(self) -> int:
        """
        Returns the number of questions in the library.
        """
        return len(self.questions)
    
    def get_categories(self) -> list:
        """
        Returns a list of the unique categories of questions in the library.
        """
        category_set = set([])
        
        for question in self.questions:    # add each question's category to the set, converting it to lowercase to eliminate duplicates
            category_set.add(question.category.lower())
        return list(category_set)

    def get_questions(self, category: str = None, difficulty: str = None, number: int = 0):
        """
        Returns a list of questions filtered by category and/or difficulty, and/or limited to a specific number of questions.
        
        Args:
        - category (str): a category to filter the questions by (default: None)
        - difficulty (str): a difficulty to filter the questions by (default: None)
        - number (int): the number of questions to return (default: 0)
        
        Returns:
        - question_list (list): list of question objects 
        """
        question_list = []
        random.shuffle(self.questions)
        
        if (number <= 0) or (number >= len(self.questions)): # if number is not specified, set it to the length of the full list of questions
            number = 0
            for question in self.questions: # loops through the questions, adding 1 to the number if they match the specified category and difficulty
                if (category in self.get_categories()) and (difficulty in ('easy', 'medium', 'hard')):
                    if (question.category.lower() == category) and (question.difficulty.lower() == difficulty):
                        number += 1
                elif (category in self.get_categories()) or (difficulty in ('easy', 'medium', 'hard')):
                    if (question.category.lower() == category):
                        number += 1
                    elif (question.difficulty.lower() == difficulty):
                        number += 1
                else:
                    number = len(self.questions) # number equals count of questions if category and difficulty is not specified
                    
        for question in self.questions: # loops through the questions, adding any that match the specified category and difficulty
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
                
            if len(question_list) == number: # returns question list when the length of the list is equal to number
                return question_list
