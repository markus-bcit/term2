import random 

class SecretWord:
    def __init__(self, secret_word=None):
        """sets the secret_word if it is not given
        Args:
            secret_word (string): self.secret_word is the secret word if not none
        """
        word_list = []
        if secret_word is not None:
            self.secret_word = secret_word
        else:
            with open('words.txt', 'r') as f:
                for word in f:
                    word_list.append(word)
            selected_word = random.choice(word_list).strip()
            self.secret_word = selected_word.upper()
    
    def show_letters(self, list_of_letters: list) -> str:
        """shows the letters that have been guessed or '_' 
        if they have not been guessed
        Args:
            list_of_letters (list): List of guessed words

        Returns:
            string: string of guessed letters with '_' in 
                    places where the letters haven't been guessed
        """
        self.list_of_letters = list_of_letters
        
        x = 0
        my_strings = []
        
        while len(self.secret_word) > x:
            my_strings.append('_')
            x += 1

        for position, letter in enumerate(self.secret_word):
            if letter.upper() in list_of_letters:
                my_strings[position] = letter.upper()

        return " ".join(str(x) for x in my_strings).upper()
    
    def check_letters(self, list_of_letters: list) -> bool:
        """Checks if the given list of letters is the word

        Args:
            list_of_letters (list): list of guessed letters

        Returns:
            bool: True if the given list of letters is the word, 
                otherwise False
        """
        
        for character in self.secret_word:
            if character.upper() not in list_of_letters:
                return False
        return True
    
    def check(self, word: str) -> bool:
        """checks if the given string matches the word

        Args:
            word (str): guessed word

        Returns:
            bool: true if the given string matches the word, otherwise False
        """
        if self.secret_word.upper() == word.upper():
            return True
        return False


class Game:
    def __init__(self, turns=10):
        self.turns = turns
        self.list = []
        self.word = SecretWord()
                
    def play_one_round(self):
        """plays a single turn and returns a boolean 

        Returns:
            function: check_letters() or check()
        """
        inputted = ''
        print(self.list)
        print(self.turns)
        
        while (inputted == '') or (not inputted.isalpha()) or (inputted in self.list):
            inputted = input("Please choose a letter or word: ").upper()
            if inputted in self.list:
                print("Letter already guessed!")

        if (len(inputted) == 1):
            self.list.append(inputted.upper())
            self.turns -= 1
            return self.word.check_letters(self.list)    
        else:
            self.turns -= 1
            return self.word.check(inputted.upper())
    
    def play(self) -> bool:
        """Loops through the play_one_round, checking if the letters/word is guessed

        Returns:
            bool: True if the letters/word is guessed
        """
        while self.turns != 0:  
            print(self.word.show_letters(self.list))
            if self.play_one_round():
                print('You win! The was:', self.word.secret_word)
                return True
        print('You lost! the word was:', self.word.secret_word) 
        return False
            
            
          
def main():
    Game().play()
    
if __name__ == '__main__':  
    main()


