from abc import *
import threading

class_lock = threading.Lock()

class Lecture():
    # lec_code, lec_year, lec_semester,lec_name, professor, lec_credits, max_students
    def __init__(self, lec_code, lec_year, lec_semester, lec_name, professor, lec_credit, max_students):
        self.code = lec_code
        self.year = int(lec_year)
        self.semester = int(lec_semester)
        self.name = lec_name
        self.professor = professor
        self.credit = int(lec_credit)
        self.max_students = int(max_students)
        self.current_students = 0
# TODO 1: 형 변환 실패 시 예외 잡기 추가해야 함

    def increment_students(self):
        if self.current_students < self.max_students:
            self.current_students += 1
            return True
        return False

    def decrement_students(self):
        if self.current_students > 0:
            self.current_students -= 1
