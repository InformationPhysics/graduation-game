import tkinter as tk
from tkinter import messagebox
import sys
sys.path.append('/Users/kim-shineui/graduation-game')

class TestView(tk.Frame):
    def __init__(self, master, main_controller):
        super().__init__(master)
        self.pack()
        self.main_controller = main_controller
        self.current_exam_index = 0
        self.button_click_count = 0

        self.start_button = tk.Button(self, text="시험 시작", font=("Helvetica", 12), command=self.start_exam)
        self.start_button.pack(pady=20)

    def start_exam(self):
        self.exams = self.main_controller.get_lecture_test()
        self.start_button.pack_forget()
        self.display_next_exam()

    def display_next_exam(self):
        if self.current_exam_index < len(self.exams):
            self.lecture, self.test = self.exams[self.current_exam_index]
            self.question_label = tk.Label(self, text=self.test.question, wraplength=300)
            self.question_label.pack(pady=20)

            self.answer_entry = tk.Entry(self)
            self.answer_entry.pack()

            self.submit_button = tk.Button(self, text="제출", command=self.submit_answer)
            self.submit_button.pack(pady=20)
        else:
            self.get_result()

    def submit_answer(self):
        user_answer = self.answer_entry.get()
        valid, result_message = self.main_controller.submit_answer(user_answer)
        self.clear_widgets()
        if valid:
            messagebox.showinfo("시험결과", result_message)
            self.get_result()
        else:
            self.current_exam_index += 1
            self.display_next_exam()

    def get_result(self):
        valid, result_message = self.main_controller.get_exam_result()
        self.result_label = tk.Label(self, text=result_message, font=("Helvetica", 16))
        self.result_label.pack(pady=20)
        if not valid:
            self.result_button = tk.Button(self, text="종료", command=self.main_controller.open_exit_window)
        else:
            self.result_button = tk.Button(self, text="다음으로", command=self.handle_button_click)

        self.result_button.pack(pady=20)

    def handle_button_click(self):
        if self.button_click_count == 0:
            self.button_click_count += 1
            self.main_controller.third_scenario()
        elif self.button_click_count == 1:
            self.main_controller.open_toeic_window()


    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()
