class Classroom:
    def __init__(self, room_name, instructor_name):
        self.room = room_name
        self.instructor = instructor_name
        self.students = []
    def __add__(self, student):
        return self.students.append(student)
    def __len__(self):
        return len(self.students)
    def __str__(self) -> str:
        return f'Room {self.room} [{self.instructor}] - {self.__len__()} students'