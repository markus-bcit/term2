
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
        self.student = Student
        self.grades = []
        self.students = []

        with open("grades.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                self.grades.append(row)

        with open("students.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                self.students.append(row)

    def find_students_by_name(self, name: str) -> list:
        """searches for students name and finds average

        Args:
            name (str): name of the student

        Returns:
            list: contains the students name id and average 
        """
        name_id_average = [] 
        name_id_grade = [] #[[name, id], [1,4,5,6,2], [name, id], [1,4,5,6,2]

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
            name_id_average.append(self.student(student[0], student[1], [
                                   eval(i) for i in student[2]]).average())

        return name_id_average

    def find_students_by_id(self, id:str) -> list:
        """Searches for student id 

        Args:
            id (str): student id of the student

        Returns:
            list: containing list of students with their 
            average scores if they match argument
        """
        name_id_average = [] 
        name_id_grade = [] 

        for col in self.students:
            for name_or_id in col:
                if id.upper() in name_or_id:
                    name_id_grade.append(col)

        for student_name_id in name_id_grade:
            for position, grade_list in enumerate(self.grades):
                if student_name_id[1] in grade_list[0]:
                    student_name_id.append(self.grades[position][1:])

        for student in name_id_grade:
            name_id_average.append(student[:2])
            name_id_average.append(self.student(student[0], student[1], [
                                   eval(i) for i in student[2]]).average())

        return name_id_average

    def print_student_list(self, full: bool=True, sort: str='name') -> print:
        """prints formatted list of all students, default storted by name 

        Args:
            full (bool, optional): displays grades if true. Defaults to True.
            sort (str, optional): 'name', 'id', or 'grade' sorts by alpha, . Defaults to 'name'.

        Raises:
            TypeError: if sort is not 'name', 'id' or 'grade'

        Returns:
            print: formatted for all student grades
        """
        name_id = self.students
        name_id_grade = []
        tmp_list = []
        for id_grade in self.grades:
            for name_id in self.students:
                if name_id[1] in id_grade[0]:
                    tmp_list.append(name_id[0])
                    tmp_list.append(name_id[1])
                    tmp_list.append(self.student(name_id[0], name_id[1], [eval(i) for i in id_grade[1:]]).average())
                    tmp_list.append(id_grade[1:])
                    name_id_grade.append(tmp_list)
                    tmp_list = []
            
        if full is False:
            for each in name_id_grade:
                each[3] = ''
        if sort.upper() == "NAME":
            name_id_grade = sorted(name_id_grade, key = lambda x: x[0]) # Sourced from https://stackoverflow.com/questions/17555218/python-how-to-sort-a-list-of-lists-by-the-fourth-element-in-each-list
        elif sort.upper() == "ID":
            name_id_grade = sorted(name_id_grade, key = lambda x: x[1], reverse=True)
        elif sort.upper() == "GRADE":
            name_id_grade = sorted(name_id_grade, key = lambda x: x[2], reverse=True)
        else:
            raise AttributeError

        for position, each in enumerate(name_id_grade):
            print(f'{name_id_grade[position][0]:<20} | {name_id_grade[position][1]} | {name_id_grade[position][2]} | {" ".join(name_id_grade[position][3])}')


def main():
    input_sort_choice = ''
    input_choice_bool = ''
    input_choice = 0
    
    while (input_choice not in (1, 2, 3)) or (input_choice_bool.upper() not in ('Y', 'YES', 'N', 'NO') or (input_sort_choice not in ('name', 'id','grade'))): #source -> Ian Stewart
        input_choice = int(input('[1] Search by student name \n[2] Search by student ID \n[3] List of student averages\nEnter [1-3]:'))
        
        if input_choice == 1:
            input_name = str(input('Please enter search: '))
            print(School().find_students_by_name(input_name))
            break
        elif input_choice == 2:
            input_id = str(input('Please enter search: '))
            print(School().find_students_by_id(input_id))
            break
        elif input_choice == 3:
            input_choice_bool = str(input('Would you like to show all grades [Y]es or [N]o: '))
            
            while input_sort_choice not in ('name', 'id', 'grade'):
                input_sort_choice = str(input("How would you like to sort by ['name', 'id', 'grade']: "))
                
                if input_choice_bool.upper() in ('Y', 'YES'):
                    School().print_student_list(True, input_sort_choice)
                    
                elif input_choice_bool.upper() in ('N', 'NO'):
                    School().print_student_list(False, input_sort_choice)

if __name__ == '__main__':
    main()