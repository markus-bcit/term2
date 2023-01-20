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

def main():
    print(show_letters_in_word("PIZZA", ["A", "I", "P", "Z"]))
    
if __name__ == "__main__":
    main()