from question import Question
from question_library import QuestionLibrary
import string

class Game:
    """A class representing a trivia game.

    Attributes:
        questions (list): A list of questions to be asked in the game.
        score (int): The player's current score in the game.
    """
    def __init__(self, filename='trivia.json', category=None, difficulty=None, number=0):
        """Initialize a new Game instance.

        Args:
            filename (str, optional): The name of the file containing the questions. Default is 'trivia.json'.
            category (str, optional): The category of questions to be included in the game. Default is None.
            difficulty (str, optional): The difficulty of questions to be included in the game. Default is None.
            number (int, optional): The number of questions to be included in the game. Default is 0.
        """
        
        self.questions = QuestionLibrary(filename).get_questions(category, difficulty, number)
        self.score = 0
        self.difficulty_score = {'easy': 1, 'medium': 2, 'hard': 3}
        
    def play(self):
        """Play the trivia game.

        The player will be asked each question in the `questions` list and their score will be updated based on their answers.
        """
        guess = 0
        for question in self.questions:
            print(question) 
            i = True
            while i == True: # loop while the answer is invalid
                guess = input('What is your guess [1-4]: ')
                if guess.isdigit() and (int(guess) <= 4) and (int(guess) > 0):
                    i = False
            if int(guess) == question.answer_id: 
                print("Correct answer!")
                self.score += self.difficulty_score[question.difficulty] # update score based on difficulty
            else: 
                print('Incorrect! The answer was:', question.correct_answer)
            print('-'*30)
            print("Your Score:", self.score)
            print('-'*30)

def main():
    Game().play()

if __name__ == '__main__':
    main()