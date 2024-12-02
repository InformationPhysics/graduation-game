class OutputView:
    @staticmethod
    def print_login_success(name):
        print(f"[SUCCESS] {name}님이 성공적으로 로그인하셨습니다.")

    @staticmethod
    def print_login_failure():
        print("[ERROR] 로그인 실패: ID 또는 비밀번호가 잘못되었습니다.")

    @staticmethod
    def print_lecture_catalog(lectures):
        print("\n=== 강의 목록 ===")
        for lecture in lectures.values():
            print(f"강의명: {lecture.name}, 코드: {lecture.code}, 현재 신청자 수: {lecture.current_students}/{lecture.max_students}")
        print("=================")

    @staticmethod
    def print_registration_success(lecture):
        print(f"[SUCCESS] {lecture.code}: 수강 신청 완료. 현재 신청자 수 {lecture.current_students}/{lecture.max_students}")

    @staticmethod
    def print_registration_failure(lecture_code):
        print(f"[ERROR] {lecture_code}: 수강 가능 인원을 초과했거나 강의 코드를 찾을 수 없습니다.")

    @staticmethod
    def print_exit_message():
        print("시스템 종료")
