"""
Instructions
This assignment is ungraded.

Animal, Cat, Dog
Create a class Animal that has the attribute "name".
Create a method on the animal class that prints "sound".
Create two child classes that inherit from Animal: Cat and Dog.
For each subclass, override the make_sound method to make it print the correct sound ("woof" or "meow", for example).
Shape, Rectangle, Square, Circle
Create the class Shape. Make sure it has an attribute "sides".
Create the class Rectangle.
make sure it inherits from Shape
a rectangle always has four sides 
its constructor should receive two values: the width and the height of the rectangle
add a method "area" that computes the area of the rectangle
Create the class Square
make sure it inherits from the best class - which are you going to choose?
Create the class Circle
make sure it inherits from Shape
its constructor receives one argument: the radius of the circle
a Circle has no sides
make sure it has an "area" method that returns the area of the square

    """

class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self, sound):
        print(sound)
        
class Cat(Animal):
    def sound(self):
        super().make_sound("meow")
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def sound(self):
        super().make_sound("woof")
     
   
d = Dog("Dog")
d.sound()
