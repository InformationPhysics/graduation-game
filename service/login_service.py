from model.student import Student
from constants.constant import ErrorMessage

class LoginService:
    file_name = "resource/student_information.md"

    def __init__(self):
        self.students_dict = {}

    def load_student_info_from_file(self):
        try:
            with open(self.file_name, "rt") as reader:
                reader.readline()  # 첫 줄 헤더 버리기
                while True:
                    line = reader.readline()
                    if not line:
                        break

                    student_info = []
                    for element in line.split(","):
                        student_info.append(element.strip())

                    if len(student_info) == 4:
                        student_id, password, name, department = student_info
                        self.students_dict[student_id] = Student(student_id, password, name, department)

        except FileNotFoundError:
            print(f"[ERROR] 파일 '{self.file_name}'을 찾을 수 없습니다.")
        return None

    def login(self, input_id, input_password):
        self.load_student_info_from_file()
        student = self.students_dict.get(input_id) # Student 인스턴스

        if student and student.password == input_password:
            return student

        return None
