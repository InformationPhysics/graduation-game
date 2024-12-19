import sys
sys.path.append("/Users/kim-shineui/graduation-game")
from model.test import Test

class TestManagementService:
    file_name = "resource/midterm_question.md"

    def __init__(self, lecture_management):
        self.lecture_management = lecture_management
        self.tests_with_lecture = {} #키: lecture 인스턴스, #값: Test(강의, 질문, 답) 인스턴스
        self.load_test_info()

    def load_test_info(self):
        try:
            with open(self.file_name, "rt") as reader:
                reader.readline()  # 첫 줄 헤더 버리기
                while True:
                    line = reader.readline()
                    if not line:
                        break
                    question_info = list(map(str.strip, line.split(",")))  # 정보 읽고 양쪽 공백 제거 후 리스트로 저장

                    if len(question_info) == 4:
                        lecture_code, lecture_name, question, answer = question_info
                        lecture = self.get_matched_lecture(lecture_code, lecture_name)

                        if lecture:
                            test = Test(question, answer)
                            self.tests_with_lecture[lecture] = test #키: 강의, 값: Test 객체

        except FileNotFoundError:
            print(f"[ERROR] 파일 '{self.file_name}'을 찾을 수 없습니다.")
            sys.exit("프로그램을 종료합니다.")

    def get_matched_lecture(self, lecture_code, lecture_name):
        lecture = self.lecture_management.find_lecture_with_code(lecture_code)
        if lecture and lecture.name == lecture_name:
            return lecture
        return None

    def find_test_with_lecture(self, lecture):
        return self.tests_with_lecture.get(lecture)

    def get_all_tests(self):
        return list(self.tests_with_lecture.values())