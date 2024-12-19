import tkinter as tk

class Scenario(tk.Toplevel):
    def __init__(self, lines, pauses=None):
        super().__init__()
        self.lines = lines
        self.pauses = pauses if pauses else []
        self.line_index = 0
        self.pause_index = 0

        self.title("대화창")
        self.text_widget = tk.Text(self, height=15, width=50)
        self.text_widget.pack()
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self._show_next_line()  # 객체 생성 시 바로 시작
        self.mainloop()

    def _show_next_line(self):
        if self.line_index < len(self.lines):
            line = self.lines[self.line_index]
            if line == '' and self.pause_index < len(self.pauses):
                message, duration, dots = self.pauses[self.pause_index]
                self.pause_index += 1
                self._animate_pause(message, duration, dots, self._show_next_line)
            else:
                self.text_widget.insert(tk.END, line + '\n')
                self.line_index += 1
                self.after(1000, self._show_next_line)

    def _animate_pause(self, message, duration, dots, callback):
        count = [0]
        def add_dot():
            if count[0] < dots:
                self.text_widget.insert(tk.END, message)
                count[0] += 1
                self.after(int(duration), add_dot)
            else:
                self.text_widget.insert(tk.END, '\n')
                self.after(1000, callback)
        add_dot()

    def _on_close(self):
        self.destroy()

class Talk1(Scenario):
    def __init__(self):
        lines = [
            '18학번으로서 어느덧 4학년 마지막 학기..',
            '지금 신입생들은 내가 입학할 당시 초등학생이었다..',
            '이제는 학교를 떠나야 할 때.. 수강신청부터 시험까지 결코 실수해서는 안된다!',
            '그런데..수강신청이 언제더라..?',
            ''  # pause
        ]
        pauses = [
            ('.', 500, 3)
        ]
        lines.append('오늘이잖아??!??!')
        super().__init__(lines, pauses)

class Talk2(Scenario):
    def __init__(self):
        lines = [
            '지옥과도 같은 티케팅을 성공적으로 마친 뒤 어느덧 약 두 달이 흘렀군',
            '중간고사가 코앞으로 다가왔다',
            '소문으로는 두 문제만 틀려도 퇴학이라는데 신중히 답을 골라야겠어..',
            '가보자!'
        ]
        super().__init__(lines)

class Talk3(Scenario):
    def __init__(self):
        lines = [
            '지금까지 완벽해 이대로면 졸업을 할 수 있을 것만 같은걸?',
            '그런데.. 왜 불길한 느낌이 들지?',
            '마치 무언갈 빼먹은 것 같은..',
            ''  # pause
        ]
        pauses = [
            ('.', 500, 3)
        ]
        lines.append('기초교양..2학점..부족..?')
        lines.append('아 맞다 토익!! 토익을 안 하고 있었어!!')
        super().__init__(lines, pauses)

class Talk4(Scenario):
    def __init__(self):
        lines = [
            '토익이 개정되어 듣기가 사라졌다니 운이 좋았군',
            '6년이라는 긴 세월..드디어 학교를 떠나는군..',
            '성인의 시작부터 지금까지 함께해온 학교야 고마워 이젠 안녕~'
        ]
        super().__init__(lines)


