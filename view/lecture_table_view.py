import tkinter as tk
from tkinter import ttk, messagebox

class LectureTableView(tk.Toplevel):
    def __init__(self, main_controller):
        super().__init__()
        self.main_controller = main_controller
        self.title("강의 목록")
        self.geometry("800x400")
        self.create_widgets()

    def create_widgets(self):
        self.lecture_table = ttk.Treeview(
            self, columns=("code", "name", "credit", "current_students", "max_students"), show="headings"
        )
        self.lecture_table.heading("code", text="강의 코드")
        self.lecture_table.heading("name", text="강의명")
        self.lecture_table.heading("credit", text="학점")
        self.lecture_table.heading("current_students", text="현재 신청자")
        self.lecture_table.heading("max_students", text="최대 정원")
        self.lecture_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 열 너비 조정
        self.lecture_table.column("code", width=100, anchor="center")
        self.lecture_table.column("name", width=200, anchor="w")
        self.lecture_table.column("credit", width=50, anchor="center")
        self.lecture_table.column("current_students", width=100, anchor="center")
        self.lecture_table.column("max_students", width=100, anchor="center")

        self.reload_button = tk.Button(self, text="강의 목록 새로고침", command=self.load_lectures)
        self.reload_button.pack(pady=10)

        self.load_lectures()

    def load_lectures(self):
        # 기존 데이터 지우기
        for row in self.lecture_table.get_children(): # treeview의 모든 항목 갖고 오기
            self.lecture_table.delete(row)

        lectures = self.main_controller.get_all_lectures()
        for lecture in lectures:
            self.lecture_table.insert(
                "", "end", values=(
                    lecture.code,
                    lecture.name,
                    lecture.credit,
                    lecture.current_students,
                    lecture.max_students
                )
            )

