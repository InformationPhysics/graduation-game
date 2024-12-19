class Student:
    def __init__(self, student_id, password, name, department):
        self.student_id = student_id
        self.password = password
        self.name = name
        self.department = department
        self.registered_lectures = [] # 강의 담는 리스트
        self.total_credits = 0

    def add_lecture(self, lecture):
        if lecture not in self.registered_lectures:
            self.registered_lectures.append(lecture)

    def remove_lecture(self, lecture):
        if lecture in self.registered_lectures:
            self.registered_lectures.remove(lecture)
