import csv
import os
class Student:
    def __init__(self, name:str, id:str, grades:list):
        self.name = name
        self.id = id
        self.grades = grades[1:]
    def average(self) -> float:
        return sum(self.grades) / len(self.grades)

class School:
    def __init__(self) -> list:
        self.grades = []
        self.students = []
        
        with open(os.path.abspath("C:/Users/Markus/OneDrive - BCIT/Desktop/Term2/ACIT 2515 Object Oriented Programming/Week4/School/grades.csv")) as f:
            reader = csv.reader(f)
            for row in reader:
                self.grades.append(row)
                
        with open(os.path.abspath("C:/Users/Markus/OneDrive - BCIT/Desktop/Term2/ACIT 2515 Object Oriented Programming/Week4/School/students.csv")) as f:
            reader = csv.reader(f)
            for row in reader:
                self.students.append(row)

    def find_students_by_name(self, name:str) -> list:
        grades = []
        for name_id in self.students:
            for name_or_id in name_id:
                if name.upper() in name_or_id.upper():
                    grades.append(name_id)
        return grades
    def find_students_by_id(self, id:str) -> list:
        pass
    def print_student_list(self, full: bool, sort: str) -> print:
        pass

print(School().find_students_by_name('Mary '))



