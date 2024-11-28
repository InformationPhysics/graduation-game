from abc import *

class AbstractStudent(metaclass=ABC):
    def __init__(self, student_number, password, name, department):
        self.student_number = student_number
        self.password = password
        self.name = name
        self.department = department
        self.lectures_registered_for = []

class Student(AbstractStudent):
    def register_lecture(self, Lecture):
        self.lectures_registered_for.append(Lecture)


