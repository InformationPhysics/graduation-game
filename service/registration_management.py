class RegistrationService:
    def register_lecture_to_student(self, student, lecture_code):
        if lecture_code in student.registered_lecture_codes:
            print(f"[ERROR] 학생 {student.name}({student.student_id})는 이미 {lecture_code}를 수강 신청했습니다.")
            return False
        student.add_lecture(lecture_code)
        print(f"[SUCCESS] 학생 {student.name}({student.student_id}): {lecture_code} 수강신청 완료.")
        return True

    def remove_sugang(self, student, lecture_code):
        student.remove_lecture(lecture_code)
