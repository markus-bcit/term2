"""
ACIT2515 Lab

Week 2 -- complete this file!

"""
import random
import string

# The number of turns allowed is a global constant
NB_TURNS = 10

def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    # WRITE YOUR CODE HERE !

    word_list = []
    with open('words.txt', 'r') as f:
        for word in f:
            word_list.append(word)
    selected_word = random.choice(word_list).strip()

    return selected_word

def show_letters_in_word(word, letters):
    """
    This function RETURNS A STRING.
    This function scans the word letter by letter.
    First, make sure word is uppercase, and all letters are uppercase.
    If the letter of the word is in the list of letters, keep it.
    Otherwise, replace it with an underscore (_).

    DO NOT USE PRINT!

    Example:
    >>> show_letters_in_word("VANCOUVER", ["A", "V"])
    'V A _ _ _ _ V _ _'
    >>> show_letters_in_word("TIM", ["G", "V"])
    '_ _ _'
    >>> show_letters_in_word("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    x = 0
    my_strings = []
    word = list(word.upper())

    while x < len(word):
        my_strings.append('_')
        x += 1

    for position, letter in enumerate(word):
        if letter in letters:
            my_strings[position] = letter

    return " ".join(str(x) for x in my_strings)

def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""
    if "_" in show_letters_in_word(word, letters):
        return False
    else:
        return True

def main(turns):
    """
    Runs the game. Allows for "turns" loops (attempts).
    At each turn:
    1. Ask the user for a letter
    2. Add the letter to the list of zletters already tried by the player
    3. If the letter was already tried, ask again
    4. Use the show_letters_in_word function to display hints about the word
    5. Remove 1 to the number of tries left
    6. Check if the player
        - won (= word has been found)
        - lost (= word has not been found, no tries left)

    Do not forget to pick a random word first :-)

    """
    # WRITE YOUR CODE HERE
    word = pick_random_word().upper()
    letter_list = []
    print('-'*20)
    print(show_letters_in_word(word, letter_list))
    while (turns > 0) and (all_letters_found(word, letter_list) == False):
        letter_input = input("Enter a letter: ").upper()
        if letter_input not in string.ascii_uppercase:
            print("WARNING: Please Enter a single letter")
        elif letter_input not in word:
            if letter_input in letter_list:
                print("WARNING: Letter already guessed")
            else:
                print("Letter not found in word, Try again!")
                turns -= 1
                letter_list.append(letter_input)
        elif letter_input in word:
            if letter_input in letter_list:
                print("WARNING: Letter already guessed")
            else:
                print("Good guess!")
                letter_list.append(letter_input)
        print(" ".join(str(x) for x in show_letters_in_word(word, letter_list)),"Guesses: ", ", ".join(str(x) for x in letter_list))
        print("Tries Remaining:", turns)
        print('-'*20)
    if (all_letters_found(word, letter_list) == False):
        print("You lost, better luck Next time")
        print("The word was: ", word)
    elif (all_letters_found(word, letter_list) == True):
        print("Congratulations!! You won!")
        
    
    

if __name__ == "__main__":
    main(NB_TURNS)