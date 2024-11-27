from abc import *

class AbstractClass(metaclass=ABC):# [코드, 연도, 학기, 강의명, 학점, 최대인원, 현재신청자수]
    def __init__(self, code, year, semester, name, credit, max_students, current_students=0):
        self.code = code
        self.year = year
        self.semester = semester
        self.name = name
        self.credit = credit
        self.max_students = max_students
        self.current_students = current_students

    # 공통 기능을 여기다가 구현
    # 구현해야 할 기능을 추상 메서드로 적기


