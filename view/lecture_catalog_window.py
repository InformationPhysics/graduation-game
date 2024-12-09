import threading
import tkinter as tk
from tkinter import ttk, messagebox
from service.lecture_management import LectureManagementService

class Lecture_Catalog_Window:
    def __init__(self, root, lecture_service):
        self.root = root
        self.lecture_service = lecture_service

    def show_class_list(self):
        lecture_catalog_window = tk.Toplevel(self.root)
        lecture_catalog_window.title("강의목록 조회")
        lecture_catalog_window.geometry("500x300") # 윈도우 크기 조정

        columns = ("강의명", "코드", "현재 신청자수")
        tree = ttk.Treeview(lecture_catalog_window, columns=columns, show='headings') # Table 형태 만들기
        tree.heading("강의명", text="강의명")
        tree.heading("코드", text="코드")
        tree.heading("현재 신청자수", text="현재 신청자수")

        tree.column("강의명", width=200, anchor="w")
        tree.column("코드", width=120, anchor="center")
        tree.column("현재 신청자수", width=100, anchor="center")

        # 데이터 삽입
        with self.lecture_service.class_lock :
            for lecture in self.lecture_service.lecture_dics.values():
                강의명 = lecture.name
                코드 = lecture.code
                현재_신청자수 = f"{lecture.current_students}/{lecture.max_students}"
                tree.insert("", tk.END, values=(강의명, 코드, 현재_신청자수))

        tree.pack(fill=tk.BOTH, expand=True)
