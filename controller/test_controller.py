class TestController:
    def __init__(self, main_controller, test_management):
        self.main_controller = main_controller
        self.test_management = test_management
        self.student = self.main_controller.current_user
        self.current_exam_index = 0  # 현재 시험 위치
        self.results = []
        self.exams = self.prepare_exams()

    def get_registered_exams(self):
        return self.exams

    def prepare_exams(self):
        return [[lecture, self.test_management.find_test_with_lecture(lecture)]
                      for lecture in self.student.registered_lectures if
                self.test_management.find_test_with_lecture(lecture)]

    def submit_answer(self, user_answer):
        if self.current_exam_index < len(self.exams):
            exam = self.exams[self.current_exam_index]
            test = exam[1]
            if user_answer.lower() == test.answer.lower():
                self.results.append(True)
            else:
                self.results.append(False)
            self.current_exam_index += 1

        if self.current_exam_index >= len(self.exams):
            return True, self.summarize_results()
        else:
            return False, None

    def summarize_results(self):
        correct_count = sum(self.results)
        return f"시험 결과: {correct_count}개 정답, {len(self.exams) - correct_count}개 오답"

    def finalize_exam(self):
        incorrect_count = len([result for result in self.results if not result])
        if incorrect_count >= 2:
            return False, "2개 이상 틀렸습니다. 퇴학입니다!"
        else:
            return True, "축하합니다! 졸업의 길이 보이기 시작했습니다!"
