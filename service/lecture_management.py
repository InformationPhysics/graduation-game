import sys
sys.path.append("/Users/kim-shineui/graduation-game")
from model.lecture import Lecture

class LectureManagementService:
    """Lecture의 데이터를 불러오고 조회한다."""

    file_name = "resource/lecture_information.md"

    def __init__(self):
        self.lectures_dict = {} # 키: 강의 코드, 값: Lecture 객체
        self.load_all_lectures()

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

    def find_lecture_with_code(self, lec_code):
        return self.lectures_dict.get(lec_code)

    def get_all_lectures(self):
        return list(self.lectures_dict.values())
