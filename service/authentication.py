from model.student import Student

class AuthenticationService:
    file_name = "resource/student_information.md"

    def __init__(self):
        self.logged_in_user = None

    def load_student_info_from_file(self, input_id):
        try:
            with open(self.file_name, "rt") as reader:
                reader.readline()  # 첫 줄 헤더 버리기
                while True:
                    line = reader.readline()
                    if not line:
                        break

                    student_info = list(map(str.strip, line.strip().split(","))) # 정보 -> list로 저장 -> 분리 후 양쪽 공백 제거
                    if len(student_info) == 4:
                        student_id, password, name, department = student_info
                        if student_id == input_id:
                            return Student(student_id, password, name, department)

        except FileNotFoundError:
            print(f"[ERROR] 파일 '{self.file_name}'을 찾을 수 없습니다.")
        return None

    def login(self, input_id, input_password):
        student = self.load_student_info_from_file(input_id) # 반환값: Student 인스턴스

        if student and student.password == input_password:
            self.logged_in_user = student
            return student

        return None