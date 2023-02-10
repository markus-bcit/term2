import random 
import json

class Question:
    """
    Class representing a question with its options and correct answer.
    """
    def __init__(self, question:str, correct_answer:str, incorrect_answers:list,category:str, difficulty:str):
        """
        Constructor for the Question class.
        
        Args:
        - question (str): the question text
        - correct_answer (str): the correct answer to the question
        - incorrect_answers (list): a list of incorrect answers
        - category (str): the category of the question
        - difficulty (str): the difficulty level of the question (either 'easy', 'medium', 'hard')
        
        Raises: 
        AttributeError: if the difficulty level is not one of 'easy', 'medium', or 'hard'
        """
        if difficulty not in ('easy', 'medium', 'hard'):
            raise AttributeError
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        incorrect_answers.append(correct_answer)
        random.shuffle(incorrect_answers)
        self.answers = incorrect_answers
        self.category = category
        self.answer_id = self.answers.index(correct_answer) + 1

    def __str__(self):
        """
        String representation of the Question object, returns the question and answers in the format:
        question text
        1 answer
        2 answer 
        3 answer 
        4 answer

        Return: 
        numbered_answered (str): the string representation of the Question object
        """
        numbered_answers = [self.question]
        for position, answer in enumerate(self.answers):
            numbered_answers.append(f'{position+1} {answer}') # position + 1 because it starts at 0 
        return ' \n'.join(numbered_answers)
