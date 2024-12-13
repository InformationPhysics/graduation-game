import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox

_cls = [
    ["PHYS3305-01", 2024, 1, "양자역학1", 3, 10, 0],
    ["PHYS2201-01", 2024, 1, "역학1", 3, 10, 0],
    ["GEC1102-S21", 2024, 1, "인간의가치탐색", 3, 20, 0],
    ["PHYS3204-00", 2024, 1, "열및통계물리1", 3, 10, 0],
    ["SOJUJOA-00", 2024, 1, "술의역사", 3, 15, 0],
    ["CHUKGUJOA-01", 2024, 1, "축구", 1, 22, 0],
    ["PHYS3203-01", 2024, 1, "전자기학2", 3, 10, 0],
    ["DISP2103-00", 2024, 1, "전자회로", 3, 10, 0],
    ["PHYS4201-00", 2024, 1, "졸업논문", 0, 100, 0],
    ["UMAYGETF-01", 2024, 1, "열및통계물리1", 3, 20, 0],
    ["PHYS3310-00", 2024, 1, "정보물리학", 3, 20, 0],
    ["GEE1345-S00", 2024, 1, "파이썬으로배우는소프트웨어코딩", 3, 20, 0],
    ["PHYS2302-00", 2024, 1, "수리물리학1", 3, 20, 0]
]

todo_sugang_list = ["PHYS3305-01", "PHYS2201-01", "PHYS3204-00", "PHYS3203-01", "PHYS4201-00"]

_st = []

stop_auto_increment = threading.Event()
cls_lock = threading.Lock()
st_lock = threading.Lock()

class Manage:
    def add_subscription(self, cls_code):
        with cls_lock:
            f_index = self.search_index(cls_code)
            if f_index == -1:
                return False, f"[ERROR] {cls_code}: 강의 코드를 찾을 수 없습니다."
            if _cls[f_index][6] >= _cls[f_index][5]:
                return False, f"[ERROR] {cls_code}: 수강 가능 인원을 초과했습니다."
            else:
                _cls[f_index][6] += 1
                return True, f"[SUCCESS] {cls_code}: 수강 신청 완료. 현재 신청자 수 {_cls[f_index][6]}/{_cls[f_index][5]}"

    def cancel_subscription(self, cls_code):
        with cls_lock:
            f_index = self.search_index(cls_code)
            if f_index != -1 and _cls[f_index][6] > 0:
                _cls[f_index][6] -= 1

    def search_index(self, cls_code):
        for i, cls in enumerate(_cls):
            if cls[0] == cls_code:
                return i
        return -1

    def get_lecture(self, cls_code):
        f_index = self.search_index(cls_code)
        return _cls[f_index][3] if f_index != -1 else None

    def auto_increment_subscriptions(self):
        while not stop_auto_increment.is_set():
            with cls_lock:
                for cls in _cls:
                    if cls[6] < cls[5]:
                        cls[6] += 1
            time.sleep(1)

class Student:
    def register(self, st_id, st_pass, st_num, st_name, st_dept, st_year):
        with st_lock:
            _st.append([st_id, st_pass, st_num, st_name, st_dept, st_year, [], 0]) 

class Sugang:
    def add_sugang_list(self, st_id, cls_code):
        with st_lock:
            f_index = self.search_index(st_id)
            if f_index == -1:
                return False, "[ERROR] 학생 ID를 찾을 수 없습니다."
            if cls_code in _st[f_index][6]:
                return False, f"[ERROR] {_st[f_index][3]}({st_id})는 이미 {cls_code}를 수강 신청했습니다."
            _st[f_index][6].append(cls_code)
            return True, f"[SUCCESS] 학생 {_st[f_index][3]}({st_id}): {cls_code} 수강신청 완료."

    def remove_sugang_list(self, st_id, cls_code):
        with st_lock:
            f_index = self.search_index(st_id)
            if f_index == -1:
                return
            if cls_code in _st[f_index][6]:
                _st[f_index][6].remove(cls_code)

    def search_index(self, st_id):
        for i, st in enumerate(_st):
            if st[0] == st_id:
                return i
        return -1

# GUI 코드
class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("수강신청 시스템")
        self.manage = Manage()
        self.sugang = Sugang()
        self.students = Student()

        self.logged_in = False
        self.logged_in_user = None
        self.auto_thread = None

        # 테스트용 학생 등록
        self.students.register("test_user", "1234", "2018103483", "홍길동", "물리학과", 3)

        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=20, pady=20)

        self.login_button = tk.Button(self.frame, text="로그인", command=self.open_login_window)
        self.sugang_button = tk.Button(self.frame, text="수강신청", command=self.open_sugang_window)
        self.classlist_button = tk.Button(self.frame, text="강의목록 조회", command=self.show_class_list)
        self.exit_button = tk.Button(self.frame, text="종료", command=self.on_exit)

        self.login_button.grid(row=0, column=0, padx=10, pady=10)
        self.sugang_button.grid(row=0, column=1, padx=10, pady=10)
        self.classlist_button.grid(row=0, column=2, padx=10, pady=10)
        self.exit_button.grid(row=0, column=3, padx=10, pady=10)

    def open_login_window(self):
        login_win = tk.Toplevel(self.master)
        login_win.title("로그인")
        tk.Label(login_win, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(login_win, text="비밀번호:").grid(row=1, column=0, padx=5, pady=5)

        id_entry = tk.Entry(login_win)
        pw_entry = tk.Entry(login_win, show="*")
        id_entry.grid(row=0, column=1, padx=5, pady=5)
        pw_entry.grid(row=1, column=1, padx=5, pady=5)

        def do_login():
            login_id = id_entry.get()
            login_pass = pw_entry.get()
            f_index = self.sugang.search_index(login_id)
            if f_index == -1:
                messagebox.showerror("오류", "[ERROR] 등록된 ID가 없습니다.")
            elif _st[f_index][1] != login_pass:
                messagebox.showerror("오류", "[ERROR] 비밀번호가 올바르지 않습니다.")
            else:
                self.logged_in = True
                self.logged_in_user = login_id
                messagebox.showinfo("로그인 성공", "[SUCCESS] 로그인 성공.")
                login_win.destroy()

        login_button = tk.Button(login_win, text="로그인", command=do_login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def open_sugang_window(self):
        if not self.logged_in:
            messagebox.showerror("오류", "[ERROR] 먼저 로그인 해주세요.")
            return

        if self.auto_thread is None:
            self.auto_thread = threading.Thread(target=self.manage.auto_increment_subscriptions, daemon=True)
            self.auto_thread.start()

        sugang_win = tk.Toplevel(self.master)
        sugang_win.title("수강신청")
        tk.Label(sugang_win, text="강의 코드:").grid(row=0, column=0, padx=5, pady=5)
        cls_code_entry = tk.Entry(sugang_win)
        cls_code_entry.grid(row=0, column=1, padx=5, pady=5)

        def do_sugang():
            cls_code = cls_code_entry.get()
            f_index_st = self.sugang.search_index(self.logged_in_user)
            if f_index_st == -1:
                messagebox.showerror("오류", "[ERROR] 학생 ID를 찾을 수 없습니다.")
                return
            f_index_cls = self.manage.search_index(cls_code)
            if f_index_cls == -1:
                messagebox.showerror("오류", f"[ERROR] {cls_code}: 강의 코드를 찾을 수 없습니다.")
                return

            course_credits = _cls[f_index_cls][4]
            current_total_credits = _st[f_index_st][7]

            if current_total_credits + course_credits > 18:
                messagebox.showerror("오류", "수강가능학점을 초과했습니다")
                return

            success, msg = self.manage.add_subscription(cls_code)
            if not success:
                messagebox.showerror("오류", msg)
                return

            success_sg, msg_sg = self.sugang.add_sugang_list(self.logged_in_user, cls_code)
            if success_sg:
                _st[f_index_st][7] += course_credits
                messagebox.showinfo("성공", msg_sg)
            else:
                self.manage.cancel_subscription(cls_code)
                messagebox.showerror("오류", msg_sg)

        tk.Button(sugang_win, text="수강신청하기", command=do_sugang).grid(row=1, column=0, columnspan=2, pady=10)

    def show_class_list(self):
        classlist_win = tk.Toplevel(self.master)
        classlist_win.title("강의목록 조회")
        # 윈도우 크기 조정 (원하는 크기로 조절 가능)
        classlist_win.geometry("500x300")

        # Treeview를 사용해 표 형태로 데이터 표시
        cols = ("강의명", "코드", "현재 신청자수")
        tree = ttk.Treeview(classlist_win, columns=cols, show='headings')

        # 각 열의 제목 설정
        tree.heading("강의명", text="강의명")
        tree.heading("코드", text="코드")
        tree.heading("현재 신청자수", text="현재 신청자수")

        # 열 너비와 정렬 설정(필요시 조정)
        tree.column("강의명", width=200, anchor="w")
        tree.column("코드", width=120, anchor="center")
        tree.column("현재 신청자수", width=100, anchor="center")

        # 데이터 삽입
        with cls_lock:
            for cls_data in _cls:
                강의명 = cls_data[3]
                코드 = cls_data[0]
                현재_신청자수 = f"{cls_data[6]}/{cls_data[5]}"
                tree.insert("", tk.END, values=(강의명, 코드, 현재_신청자수))

        tree.pack(fill=tk.BOTH, expand=True)

    def on_exit(self):
        stop_auto_increment.set()
        if self.auto_thread is not None:
            self.auto_thread.join()
        if self.logged_in_user is not None:
            f_index = self.sugang.search_index(self.logged_in_user)
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
        
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
