import string

class Person:
    def __init__(self, name, age):
        for character in str(name):
            if character not in string.ascii_letters + ' ':
                raise AttributeError
        if len(name)< 3:
            raise AttributeError
        if not isinstance(age, int) or (age <= 0):
            raise AttributeError
        
        self.name = name
        self.age = age
        
    def get_name(self):
        return f'{self.name.upper()} / {self.age}'
    
def main():
    a = Person
    print(a(12345,123))
if __name__ == '__main__':
    main()