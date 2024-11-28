from model.student import Student

class InputView():

    @staticmethod
    def sign_up_student(self):
        print("\n=== 학생 등록 ===")
        student_number = input("학번: ")
        password = input("비밀번호: ")
        name = input("이름: ")
        department = input("학과: ")

        # 중복 검사(유효성) 추가 해야 함
        print(f"[SUCCESS] 학생 {name}({student_number}) 등록 완료.")
        return Student(student_number, password, name, department)
