"""
Inheritience 
"""
class Parent:
    def hello(self):
        print("Hello")

class Child(Parent):
    def another_hello(self):
        print('CHILD')
    pass

c = Child()
c.hello() # -> Hello
c.another_hello() # -> CHILD

#####################################################

class Child(Parent):
    def hello(self):
        super().hello() # -> gives access to access to any method
        print('CHILD')

p = Parent()
c = Child()

c.hello() # -> CHILD
p.hello() # -> Hello

##########################################################

class Person:
    
    def __init__(self, name):
        self.name = name 
        
    def greet(self):
        print("Hello, my name is ", self.name)

class Student(Person): # -> student is a person 
    
    def __init__(self, name, student_id):
        super().__init__(name) # -> calls back to the person __init__
        self.student_id = student_id
        
    def greet(self):
        super().greet() # -> gives access to access to any method
        print('I am a student and my student id is:', self.student_id)
        
s = Student('Markus', "a123456789")

s.name # -> prints the "name"
s.greet()
