class Lecture:
    def __init__(self, lec_code, lec_year, lec_semester, lec_name, professor, lec_credit, max_students):
        self.code = lec_code
        self.year = lec_year
        self.semester = lec_semester
        self.name = lec_name
        self.professor = professor
        self.credit = int(lec_credit)
        self.max_students = int(max_students)
        self.current_students = 0

    def increment_students(self):
        if self.current_students < self.max_students:
            self.current_students += 1

    def decrement_students(self):
        if self.current_students > 0:
            self.current_students -= 1
