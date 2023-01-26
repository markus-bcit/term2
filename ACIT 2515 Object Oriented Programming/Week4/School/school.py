import csv
import os

class Student:
    def __init__(self, name:str, id:str, grades:list):
        self.name = name
        self.id = id
        self.grades = grades
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
            next(reader)
            for row in reader:
                self.students.append(row)

    def find_students_by_name(self, name:str) -> list:
        name_id_average = []
        name_id_grade = []
        
        for col in self.students:
            for name_or_id in col:
                if name.upper() in name_or_id.upper():
                    name_id_grade.append(col)
                    
        for studentname_id in name_id_grade:
            for position, grade_list in enumerate(self.grades):
                if studentname_id[1] in grade_list[0]:
                    studentname_id.append(self.grades[position][1:])
                    
        for student in name_id_grade:
            name_id_average.append(student[:2])
            name_id_average.append(Student(student[0], student[1], [eval(i) for i in student[2]]).average())
        
        return name_id_average
    
    def find_students_by_id(self, id:str) -> list:
        id_grade = []
        id_average = []
                           
        for position, grade_list in enumerate(self.grades):
            if id in grade_list[0]:
                id_grade.append(self.grades[position])
        
        for position, id in enumerate(id_grade):
                id_average.append(id_grade[position][0])
                id_average.append(Student(None, id_grade[position][0], [eval(i) for i in id_grade[position][1:]]).average())
                
        return id_average
    def print_student_list(self, full: bool, sort: str) -> print:
        pass
    
    
def main():
    print(School().find_students_by_name('Marc'))
    print(School().find_students_by_id('973'))
    
if __name__=='__main__':
    main()



