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

    def get_student(self):

# TODO 1: 학생정보를 파일에 저장하는 방식 고민하기
# TODO 2: 학번 유효성 검사, 비밀번호 재확인, 비밀번호 안 보이게 하기


