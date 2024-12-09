import threading
import tkinter as tk
from tkinter import ttk, messagebox
from constant.constant import ErrorMessage

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("수강신청 시스템")
        self.is_logged_in = False
        self.auto_thread = None

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.login_button = tk.Button(self.frame, text="로그인", command=self.open_login_window)
        self.registration_button = tk.Button(self.frame, text="수강신청", command=self.open_registration_window)
        self.class_catalog_button = tk.Button(self.frame, text="강의목록 조회", command=self.show_class_list)
        self.exit_button = tk.Button(self.frame, text="종료", command=self.on_exit)

        self.login_button.grid(row=0, column=0, padx=10, pady=10)
        self.registration_button.grid(row=0, column=1, padx=10, pady=10)
        self.class_catalog_button.grid(row=0, column=2, padx=10, pady=10)
        self.exit_button.grid(row=0, column=3, padx=10, pady=10)


    def on_exit(self):
        stop_auto_increment.set()
        if self.auto_thread is not None:
            self.auto_thread.join()
        if self.user_logged_in is not None:
            f_index = self.sugang.search_index(self.user_logged_in)
            if f_index != -1:
                sugang_list = _st[f_index][6]
                msg = "\n=== 수강 신청한 과목 목록 ===\n"
                for cls_code in sugang_list:
                    lecture_name = self.manage.get_lecture(cls_code)
                    if lecture_name:
                        msg += f"강의명: {lecture_name} (코드: {cls_code})\n"
                msg += "=================\n"

                if set(sugang_list) == set(todo_sugang_list):
                    state = 0
                elif set(todo_sugang_list).issubset(set(sugang_list)):
                    state = 1
                else:
                    state = -1

                if state == 0:
                    msg += "휴…큰일 날 뻔 했다.. 한학기 더 할 뻔 했는데..\n"
                    msg += "듣고 싶은 과목이 좀 더 있었는데 아쉽다..졸업엔 영향 없겠지?\n"
                    msg += "양자..역학..열통..졸논.. 전자기.. 학점은 다 채웠고..뭐 빠진 건 없겠지?\n"
                    msg += "음? 기본교양 3/4..? 설마..??? 맞다 토익!!\n"
                    msg += "다행이도 다음주에 신청할 수 있군..근데 마지막이네..반드시 성공하여 인생의 장대한 서막을 울리리라\n"
                    msg += "TOEIC GOGO\n"

                messagebox.showinfo("수강신청 결과", msg)

        self.root.quit()
