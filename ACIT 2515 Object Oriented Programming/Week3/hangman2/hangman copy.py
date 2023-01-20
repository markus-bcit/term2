import random

class SecretWord:
    def __init__(self, secret_word=None):
        self.secret_word = secret_word
        if secret_word is None:
            
            word_list = []
            
            with open('words.txt', 'r') as f:
                for word in f:
                    word_list.append(word)
            selected_word = random.choice(word_list)
            self.secret_word = selected_word.upper()
    
    def show_letters(self, list_of_letters):
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
    
    def check_letters(self, list_of_letters):
        
        for character in self.secret_word:
            if character.upper() not in list_of_letters:
                return False
        return True
    
    def check(self, word):
        if self.secret_word.upper() == word.upper():
            return True
        return False


class Game:
    def __init__(self, turns=10):
        self.turns = turns
        self.list = []
        self.word = SecretWord()
        
    def play_one_round(self):
        inputted = ''
        valid_input = False
        print(self.list)
        print(self.turns)
        
        while valid_input == False:
            inputted = input("Please choose a letter or word: ").upper()
            if not inputted:
                print("Please input a letter or word") 
            elif not inputted.isalpha():
                print('PLease enter a letter or word')
            elif inputted in self.list:
                print("Letter already guessed") 
            else:
                valid_input = True
                
        if (len(inputted) == 1):
            self.list.append(inputted.upper())
            self.turns -= 1
            return self.word.check_letters(self.list)    
        else:
            self.turns -= 1
            return self.word.check(inputted)
    
    def play(self):
        print(self.word.secret_word)
        while self.turns > 0:  
            print(self.word.show_letters(self.list))
            if Game.play_one_round(self):
                print('You win')
                return True
        print('L the word was:', self.word.secret_word) 
        return False
            
            
          
def main():   
    SecretWord('asdf') 
    Game().play()
    
if __name__ == '__main__':  
    main()


