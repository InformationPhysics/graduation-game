import tkinter as tk
from tkinter import messagebox
import sys
sys.path.append('/Users/kim-shineui/graduation-game')
from model.student import Student

class TestApp:
    def __init__(self, root, student):
        self.root = root
        self.student = student
        self.results = []  # 각 시험 결과 저장 (1: 정답, 0: 오답)
        self.state = True  # 최종 상태 (True: 합격, False: 퇴학)

        # 과목 정보 읽기
        self.all_courses = self.load_courses_from_md("resource/lecture_information.md")

        # 과목코드 -> (과목명, ...) 맵핑
        self.course_map = {course[0]: course for course in self.all_courses}

        # 문제/정답 매핑 (과목명 기준)
        # 주어진 문제를 과목명과 매칭
        self.questions_map_by_name = {
            "양자역학1": ("양자역학1 문제: '슈뢰딩거 방정식을 만든 사람은?", "슈뢰딩거"),
            "역학1": ("역학1 문제: F=ma에서 a는?", "가속도"),
            "인간의가치탐색": ("인간의가치탐색 문제: 너 자신을 알라고 한 철학자이자 훌륭한 야구선수는?", "소크라테스"),
            "열및통계물리1_1": ("열및통계물리1 문제: 열역학은 총 몇개의 법칙이 있나? ~개로 답하시오", "4개"),
            "술의역사": ("술의역사 문제:버번의 주 재료는?", "옥수수"),
            "축구": ("축구 문제: 축구 필드 내에는 통상적으로 몇명이 뛰나? ~명으로 답하시", "23명"),
            "전자기학2": ("전자기학2 문제: 그리피스의 fist name 은?", "David"),
            "졸업논문": ("졸업논문 문제: 졸업논문을 꼭 써야만 할까? 예/아니오로 답하시오.", "아니오"),
            "열및통계물리1_2": ("열및통계물리1 문제: 리만가설을 증명하시오", "어딜졸업하려고"),
            "정보물리학": ("정보물리학 문제: 정보물리학은 몇 학년 과목일까요?", "1학년"),
            "파이썬으로배우는소프트웨어코딩": ("파이썬으로배우는소프트웨어코딩 문제: print(a)", "NameError"),
            "수리물리학1": ("수리물리학1 문제: 정진모 교수님이 사용하시는 수리물리학 교재는?", "아프켄")
        }

        # 중복되는 "열및통계물리1" 과목 처리를 위해 과목코드별로 문제를 할당
        # PHYS3204-00 첫번째 열및통계물리1
        # UMAYGETF-01 두번째 열및통계물리1
        # 나머지는 과목명으로 바로 매핑
        self.questions_dict = {}
        for code, data in self.course_map.items():
            course_name = data[3]
            if course_name == "열및통계물리1":
                # 첫번째 등장: PHYS3204-00
                # 두번째 등장: UMAYGETF-01
                # 이를 구분하기 위해 조건문 사용
                if code == "PHYS3204-00":
                    self.questions_dict[code] = self.questions_map_by_name["열및통계물리1_1"]
                elif code == "UMAYGETF-01":
                    self.questions_dict[code] = self.questions_map_by_name["열및통계물리1_2"]
            else:
                # 과목명이 그대로 매핑 가능하면
                if course_name in self.questions_map_by_name:
                    self.questions_dict[code] = self.questions_map_by_name[course_name]

        # 학생이 신청한 과목 중 문제 있는 과목 필터
        self.selected_courses = [code for code in self.student.registered_lectures if code in self.questions_dict]

        self.current_exam = 0  # 현재 시험 인덱스
        self.create_main_ui()

    def load_courses_from_md(self, filename):
        courses = []
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # 첫 줄은 헤더이므로 skip
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            parts = [x.strip() for x in line.split(',')]
            # parts: [강의코드, 년도, 학기, 강의명, 교수명, 학점, 최대수강인원]
            if len(parts) == 7:
                course_code, year, semester, course_name, professor, credits, max_students = parts
                year = int(year)
                semester = int(semester)
                credits = int(credits)
                max_students = int(max_students)
                courses.append([course_code, year, semester, course_name, professor, credits, max_students])
        return courses

    def create_main_ui(self):
        tk.Label(self.root, text="시험을 시작하려면 아래 버튼을 누르세요.", font=("Helvetica", 12)).pack(pady=20)
        tk.Button(self.root, text="시험 시작", command=self.start_exam, font=("Helvetica", 14)).pack()

    def start_exam(self):
        if not self.selected_courses:
            messagebox.showinfo("안내", "학생이 신청한 강의 중 시험 가능한 과목이 없습니다.")
            return
        self.run_exam(self.current_exam)

    def run_exam(self, exam_index):
        if exam_index >= len(self.selected_courses):
            self.finalize()
            return

        course_code = self.selected_courses[exam_index]
        question, answer = self.questions_dict[course_code]

        exam_window = tk.Toplevel(self.root)
        exam_window.title(f"{course_code} 시험")

        tk.Label(exam_window, text=question, font=("Helvetica", 16), wraplength=400, justify="left").pack(pady=10)

        answer_entry = tk.Entry(exam_window, font=("Helvetica", 14))
        answer_entry.pack(pady=10)

        def submit_answer():
            user_answer = answer_entry.get().strip()
            if not user_answer:
                messagebox.showerror("오류", "답변을 입력하세요!")
                return

            if user_answer == answer:
                self.results.append(1)
                print(f"{course_code} 과목 결과: 1 (정답)")
            else:
                self.results.append(0)
                print(f"{course_code} 과목 결과: 0 (오답)")

            exam_window.destroy()
            self.current_exam += 1
            self.run_exam(self.current_exam)

        tk.Button(exam_window, text="제출", command=submit_answer, font=("Helvetica", 14)).pack(pady=10)

    def finalize(self):
        incorrect_count = self.results.count(0)
        if incorrect_count >= 2:
            self.state = False
            messagebox.showwarning("결과", "2개 이상 틀렸습니다. 퇴학입니다!")
        else:
            self.state = True
            messagebox.showinfo("결과", "축하합니다! 졸업의 길이 보이기 시작했습니다!")
        print(f"최종 결과: {'성공' if self.state else '퇴학'}")


if __name__ == "__main__":
    # 예시 학생 생성
    student = Student("20240001", "password123", "홍길동", "물리학과")

    # 학생이 신청한 강의 추가 (예시)
    student.add_lecture("PHYS3305-00")     # 양자역학1
    student.add_lecture("PHYS2201-00")     # 역학1
    student.add_lecture("CHUKGUJOA-01")    # 축구
    student.add_lecture("PHYS3203-01")     # 전자기학2
    student.add_lecture("PHYS2302-00")     # 수리물리학1 (교수명 부분 쉼표 처리 이슈 수정)

    root = tk.Tk()
    root.title("시험 시스템")
    root.geometry("450x200")

    app = TestApp(root, student)
    root.mainloop()

