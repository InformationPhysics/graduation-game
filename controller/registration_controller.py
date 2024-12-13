from service.lecture_management import LectureManagementService
from service.registration_management import RegistrationService
import threading

class RegistrationController:
    def __init__(self):
        self.current_user = None
        self.lecture_management = LectureManagementService()
        self.registration_service = RegistrationService()
        self.auto_thread = None

    def get_all_lectures(self):
        return self.lecture_management.get_all_lectures()

    def start_auto_increment(self):
        if not self.auto_thread or not self.auto_thread.is_alive():
            self.auto_thread = threading.Thread(
                target=self.lecture_management.auto_increment_subscriptions,
                daemon=True
            )
            self.auto_thread.start()

    def register_lecture(self, current_user, lecture_code):
        self.current_user = current_user
        lecture = self.lecture_management.find_lecture_with_code(lecture_code)

        if not lecture:
            return False, f"[ERROR] {lecture_code}: 강의 코드를 찾을 수 없습니다."

        if self.current_user.total_credits + lecture.credit > 18:
            return False, "수강 가능 학점을 초과했습니다."

        success, msg = self.lecture_management.add_subscription(lecture_code)
        if not success:
            return False, msg

        success_sg, msg_sg = self.registration_service.register_lecture_to_student(self.current_user, lecture_code)
        if success_sg:
            self.current_user.total_credits += lecture.credit
            return True, msg_sg
        else:
            self.lecture_management.cancel_subscription(lecture_code)
            return False, msg_sg
