from constants.choice import Choice

class InputView:
    @staticmethod
    def get_choice():
        print("\n=== 수강신청 시스템 ===")
        print(f"{Choice.LOGIN}. 로그인")
        print(f"{Choice.ADD_LECTURE}. 수강 신청")
        print(f"{Choice.SHOW_LECTURES}. 강의 목록 보기")
        print(f"{Choice.EXIT}. 종료")
        return input("선택: ")

    @staticmethod
    def get_login_info():
        student_id = input("로그인 ID: ")
        password = input("비밀번호: ")
        return student_id, password

    @staticmethod
    def get_course_code():
        return input("수강할 강의 코드: ")