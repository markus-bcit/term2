"""Student class
A instance of the Student class must contain:

the name of the student
the student ID
the list of grades for the student
The Student class must also have a way to compute the average grade for the student.

School class
The School class takes no arguments for the constructor.

It reads from the students.csv file and generate Student instances as required. The grades for the students are available in the file grades.csv.

A school instance must have methods for the following behaviours:

find_students_by_name: takes a string, returns a list containing all student instances whose name match the argument provided (regardless of case)
find_students_by_id: takes a string, returns a list containing all student instances whose student ID is equal to the argument provided
print_student_list: prints a list on the screen showing all students with their name, student ID and average grade. The method takes optional parameters:
full: boolean - if True, display all the grades for each student too
sort: string - if it is one of "name", "id", or "average", sort the returned list by the relevant attribute
Add a short block of code in the "if __name__ == '__main__'" block of your program that demonstrates how it works.

Submit your files and a class diagram for your program.

Grading
4 marks for code quality and cleanliness (includes comments and docstrings)
4 marks for the School class
2 marks for the Student class"""
import csv
import os


class Student:
    def __init__(self, name: str, id: str, grades: list):
        self.name = name
        self.id = id
        self.grades = grades

    def average(self) -> float:
        """Returns the average of self.grades

        Returns:
            float: average of self.grades
        """
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

    def find_students_by_name(self, name: str) -> list:
        """_summary_

        Args:
            name (str): name of the student

        Returns:
            list: contains the students name id and average 
        """
        name_id_average = []
        name_id_grade = []

        for col in self.students:
            for name_or_id in col:
                if name.upper() in name_or_id.upper():
                    name_id_grade.append(col)

        for student_name_id in name_id_grade:
            for position, grade_list in enumerate(self.grades):
                if student_name_id[1] in grade_list[0]:
                    student_name_id.append(self.grades[position][1:])

        for student in name_id_grade:
            name_id_average.append(student[:2])
            name_id_average.append(Student(student[0], student[1], [
                                   eval(i) for i in student[2]]).average())

        return name_id_average

    def find_students_by_id(self, id:str) -> list:
        id_grade = []
        id_average = []

        for position, grade_list in enumerate(self.grades):
            if id in grade_list[0]:
                id_grade.append(self.grades[position])

        for position, id in enumerate(id_grade):
            id_average.append(id_grade[position][0])
            id_average.append(Student(None, id_grade[position][0], [
                              eval(i) for i in id_grade[position][1:]]).average())

        return id_average

    def print_student_list(self, full: bool=True, sort: str='name') -> print:
        """prints formatted list of all students, default storted by name 

        Args:
            full (bool, optional): _description_. Defaults to True.
            sort (str, optional): 'name', 'id', or 'grade' sorts by alpha, . Defaults to 'name'.

        Raises:
            TypeError: if sort is not 'name', 'id' or 'grade'

        Returns:
            print: formated for all student grades
        """
        name_id = self.students
        name_id_grade = []
        tmp_list = []
        for position, grade in enumerate(self.grades):
            tmp_list.append(name_id[position][0])
            tmp_list.append(name_id[position][1])
            tmp_list.append(Student(None, None, [eval(i) for i in grade[1:]]).average())
            tmp_list.append(grade[1:])
            name_id_grade.append(tmp_list)
            tmp_list = []
            
        if full is False:
            for each in name_id_grade:
                each[3] = ''
        if sort.upper() == "NAME":
            name_id_grade = sorted(name_id_grade, key = lambda x: x[0])
        elif sort.upper() == "ID":
            name_id_grade = sorted(name_id_grade, key = lambda x: x[1], reverse=True)
        elif sort.upper() == "GRADE":
            name_id_grade = sorted(name_id_grade, key = lambda x: x[2], reverse=True)
        else:
            raise AttributeError

        for position, each in enumerate(name_id_grade):
            print(f'{name_id_grade[position][0]:<20} | {name_id_grade[position][1]} | {name_id_grade[position][2]} | {" ".join(name_id_grade[position][3])}')
                


def main():
    School().print_student_list()
    print()
    School().print_student_list(False, 'id')
    print()
    School().print_student_list(True, 'grade')



if __name__ == '__main__':
    main()
