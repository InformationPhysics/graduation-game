class Student:
    def __init__(self, student_id, password, name, department):
        self.student_id = student_id
        self.password = password
        self.name = name
        self.department = department
        self.registered_lecture_codes = [] # 강의 코드 담는 리스트
        self.total_credits = 0

    def add_lecture(self, lecture_code):
        if lecture_code not in self.registered_lecture_codes:
            self.registered_lecture_codes.append(lecture_code)

    def remove_lecture(self, lecture_code):
        if lecture_code in self.registered_lecture_codes:
            self.registered_lecture_codes.remove(lecture_code)

# TODO 1: 학번 유효성 검사, 비밀번호 재확인, 비밀번호 안 보이게 하기


