import csv
        
class Student:
    
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = list(grades)
        
    def compute_average(self):
        """Computes the average of self.grades

        Returns:
            float: gives the average of self.grades
        """
        return sum(self.grades) / len(self.grades)

class School:
    def __init__(self):
        self.students = []
        self.grades = []
        self.student = Student
        
        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.students.append(row)
        with open('grades.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:            
                    self.grades.append(row) 
    
    def find_students_by_name(self, name):
        """A method that finds students by name returns their grades

        Args:
            name (str): name of the student

        Returns:
            list: list of matching students with their grade appended
        """
        matching_students = []
        
        for student in self.students:
            if name.lower() in student[0].lower():
                matching_students.append(student)


        for student_grade in matching_students:
            for position, grade_list in enumerate(self.grades):
                if student_grade[1] in grade_list[0]:
                    student_grade.append(self.grades[position][1:])
            
    def find_students_by_id(self, student_id):
        """Method that finds students by id returns their grades

        Args:
            student_id (str): the id of the student
        """
        matching_students = []
        
        for student in self.students:
            if student_id in student[1]:
                matching_students.append(student)

        for student_grade in matching_students:
            for position, grade_list in enumerate(self.grades):
                if student_grade[1] in grade_list[0]:
                    student_grade.append(self.grades[position][1:])    
    
    def print_student_list(self, full: bool = True, sort='name'):
        """This function prints the list of students based on the given parameters

        Args:
            full (bool, optional): Indicates whether the grades should be included in the output. Defaults to True.
            sort (str, optional): Indicates the sort order of the students, can be name 'name','id','grade'. Defaults to 'name'.
        """
        self.grades
        self.students

        list_a = []
        list_b = []
        for grade in self.grades:
            for student in self.students:
                if student[1] == grade[0]:
                    list_a.append(student[0])
                    list_a.append(student[1])
                    list_a.append(Student(student[0], student[1], [eval(i) for i in grade[1:]]).compute_average())
                    list_a.append(grade[1:])
                    list_b.append(list_a)
                    list_a = []

        if full is False:
            if sort == "name":
                list_b = sorted(list_b, key=lambda x: x[0])
            elif sort == "id":
                list_b = sorted(list_b, key=lambda x: x[1])
            elif sort == "grade":
                list_b = sorted(list_b, key=lambda x: x[2]) 
        
            for student in list_b:
                print(f"{student[0]}, {student[1]}, {student[2]}, {student[3]}")

        # if full is False:
        #     for student in list_b:
        #         if sort == "name":
        #             list_b = sorted(list_b, key=lambda x: x[0])
        #         elif sort == "id":
        #             list_b = sorted(list_b, key=lambda x: x[1])
        #         elif sort == "grade":
        #             list_b = sorted(list_b, key=lambda x: x[2]) 
        #         for student in list_b:
        #             print(f"{list_b[0]}, {list_b[1]}, {list_b[2]}")

                    
def main():
    
    School().print_student_list()
    print()
    School().print_student_list(True, "grade")
    print()
    School().print_student_list(False, "id")

if __name__ == '__main__':
    main()

"""   
couple things here `
        if full is False:
            for student in list_b:
                if sort == "name":
                    list_b = sorted(list_b, key=lambda x: x[0])
                elif sort == "id":
                    list_b = sorted(list_b, key=lambda x: x[1])
                elif sort == "grade":
                    list_b = sorted(list_b, key=lambda x: x[2]) 
                for student in list_b:
                    print(f"{list_b[0]}, {list_b[1]}, {list_b[2]}")`

you dont need a for loop here because the list is already a list of list.
also you have for student in list_b twice so that is causing issues. print
has list_b not students so instead its printing list_b for every student
`
        if full is False:
            if sort == "name":
                list_b = sorted(list_b, key=lambda x: x[0])
            elif sort == "id":
                list_b = sorted(list_b, key=lambda x: x[1])
            elif sort == "grade":
                list_b = sorted(list_b, key=lambda x: x[2]) 
        
            for student in list_b:
                print(f"{student[0]}, {student[1]}, {student[2]}")`"""