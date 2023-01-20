import string

def str2dict(text):
    letter_dict = {}
    for character in text:
        if character in letter_dict:
            letter_dict[character] += 1
        elif character not in letter_dict:
            letter_dict[character] = 1
    return letter_dict

def str2dict_plus(text):
    new_text = ''
    for character in text:
        if character not in string.punctuation + ' ':
            new_text += character
    return str2dict(new_text)

def histogram(text_dict):
    for item in text_dict:
        print(item, '*'*text_dict[item])
    
def main():
    text = "Hello world!"
    histogram(str2dict_plus(text))

if __name__ == '__main__':
    main()

    