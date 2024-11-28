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

# 강의 목록을 캡슐화, 탐색 속도 증가하기 위해 사용할 예정
# 다만 정적으로 미리 선언하던가 데이터베이스를 쓰는게 좋을 것 같음
class LectureManager():
    def __init__(self):
        self.lectures = {}

    def add_lecture(self, lecture): # 강의를 dictionary 형태로 저장한다. 이때 key 값을 강의 코드로 저장하게 한다.
        if lecture.code in self.lectures:
            raise ValueError(f"강의 코드 {lecture.code}는 이미 존재합니다.")
        self.lectures[lecture.code] = lecture

    def remove_lecture(self, lecture_code):
        if lecture_code in self.lectures:
            del self.lectures[lecture_code]
        else:
            raise ValueError(f"강의 코드 {lecture_code}를 찾을 수 없습니다.")

    def find_lecture(self, lecture_code):
        return self.lectures.get(lecture_code, None)

    def list_all_lectures(self):
        return list(self.lectures.values())
