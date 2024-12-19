import threading

class RegistrationController:
    def __init__(self, lecture_management, main_controller):
        self.lecture_management = lecture_management
        self.main_controller = main_controller
        self.register_lock = threading.Lock()
        self.auto_thread = None

    def register_lecture_with_user(self, current_user, lecture_code):
        """수강 가능할 때 강의 수강인원 증가, 학생의 수강 강의 리스트에 해당 강의를 추가한다"""

        lecture = self.lecture_management.find_lecture_with_code(lecture_code)
        if not lecture:
            return False, f"[ERROR] {lecture_code}: 강의 코드를 찾을 수 없습니다."

        with self.register_lock:
            if lecture in current_user.registered_lectures:
              return False, "[ERROR] 이미 수강하고 있는 강의입니다."
            if current_user.total_credits + lecture.credit > 18:
                return False, "[ERROR] 수강 가능 학점을 초과했습니다."
            if lecture.current_students >= lecture.max_students:
                return False, "[ERROR] 수강 인원이 초과되었습니다."

            lecture.current_students += 1
            current_user.add_lecture(lecture)
            current_user.total_credits += lecture.credit

            self.main_controller.update_user_info(current_user)
            return True, f"[SUCCESS] 학생 {current_user.name}({current_user.student_id}): {lecture.name} 수강 신청 완료."

    def start_auto_increment(self):
        """자동 증가 스레드 시작"""
        if not self.auto_thread or not self.auto_thread.is_alive(): # 체크
            self.auto_thread = threading.Thread(
                target=self.auto_increment_subscriptions,
                daemon=True
            )
            self.auto_thread.start()

    def auto_increment_subscriptions(self):
        """강의의 현재 수강 인원을 자동으로 증가시킨다."""
        while True:
            with self.register_lock:
                for lecture in self.lecture_management.get_all_lectures():
                    if lecture.current_students < lecture.max_students:
                        lecture.current_students += 1
            threading.Event().wait(5)
