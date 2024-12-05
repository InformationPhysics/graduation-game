from model.lecture import Lecture
import threading

class LectureManagementService:
    file_name = "resource/lecture_information.md"

    def __init__(self):
        self.lectures_dict = {} # 키: 강의코드, 값: Lecture 객체
        self.load_all_lectures()
        self.lock = threading.Lock()

    def load_all_lectures(self):
        try:
            with open(self.file_name, "rt") as reader:
                reader.readline()  # 첫 줄 헤더 버리기
                while True:
                    line = reader.readline()
                    if not line:
                        break

                    lecture_info = list(map(str.strip, line.split(","))) # 정보 읽고 양쪽 공백 제거 후 리스트로 저장
                    if len(lecture_info) == 7:
                        lec_code, lec_year, lec_semester,lec_name, professor, lec_credits, max_students = lecture_info
                        lecture = Lecture(lec_code, lec_year, lec_semester,lec_name, professor, lec_credits, max_students)
                        self.lectures_dict[lec_code] = lecture

        except FileNotFoundError:
            print(f"[ERROR] 파일 '{self.file_name}'을 찾을 수 없습니다.")

    def add_subscription(self, lecture_code):
        with self.lock:
            lecture = self.lectures_dict.get(lecture_code)
            if lecture and lecture.increment_students():
                return lecture
        return None

    def cancel_subscription(self, lecture_code):
        with self.lock:
            lecture = self.lectures_dict.get(lecture_code)
            if lecture:
                lecture.decrement_students()

    def auto_increment_subscriptions(self):
        while True:
            with self.lock:  # 락으로 보호하여 수강 인원 증가 작업 중에 데이터가 변경되지 않도록 함
                for lecture in self.lectures_dict.values():
                    if lecture.increment_students():
                        pass
            threading.Event().wait(1)  # 1초 대기
