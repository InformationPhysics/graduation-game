from abc import *
import threading

class_lock = threading.Lock()

class AbstractLecture(metaclass=ABC):# [코드, 연도, 학기, 강의명, 학점, 최대인원, 현재신청자수]
    def __init__(self, code, year, semester, name, credit, max_students, current_students=0):
        self.code = code
        self.year = year
        self.semester = semester
        self.name = name
        self.credit = credit
        self.max_students = max_students
        self.current_students = current_students

    @abstractmethod
    def add_number_of_subscription(self, class_code):
        with class_lock:
            pass

    @abstractmethod
    def cancel_subscription(self, class_code):
        with class_lock:
            pass

    @abstractmethod
    def search_class_index_by_code(self, class_code):
        pass

class Lecture(AbstractLecture):
     # 메서드 추가하기, 추상 메서드 구현하기

lectures = [
    Lecture("a", 2024, 1, "양자역학1", 3, 10, 0),
    Lecture("b", 2024, 1, "역학1", 3, 10, 0),
    Lecture("c", 2024, 1, "인간의가치탐색", 3, 20, 0),
    Lecture("d", 2024, 1, "열및통계물리1", 3, 10, 0),
    Lecture("e", 2024, 1, "술의역사", 3, 15, 0),
    Lecture("f", 2024, 1, "축구", 1, 22, 0),
]