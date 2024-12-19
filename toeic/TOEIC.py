import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import base64
from io import BytesIO

class TOEIC:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OMR Viewer")

        image_frame = tk.Frame(self.root)
        image_frame.pack(side='left')
        self.canvas = tk.Canvas(image_frame, width=600, height=400)  # 일단 기본 크기로 설정
        self.canvas.pack()
        self.load_image()

        self.questions = [101, 102, 103, 104]
        self.options = ['A', 'B', 'C', 'D']
        self.correct_answers = ['D', 'A', 'B', 'C']
        self.user_answers = {question: tk.StringVar(value='') for question in self.questions}
        self.setup_omr_frame()

        self.root.mainloop()

    def load_image(self):
        # Base64로 인코딩된 이미지 데이터
        from toeic.image_texted import encoded_image
        image_data = encoded_image

        # Base64 문자열을 이미지로 디코딩
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes)).convert('RGB')
        self.photo = ImageTk.PhotoImage(image)

        # Canvas에 이미지 표시
        self.canvas.config(width=self.photo.width(), height=self.photo.height())
        self.canvas.create_image(0, 0, anchor='nw', image=self.photo)

    def setup_omr_frame(self):
        omr_frame = tk.Frame(self.root)
        omr_frame.pack(side='right', padx=20)

        tk.Label(omr_frame, text="정답을 선택하세요").grid(row=0, column=0, columnspan=5, pady=10)

        for i, question in enumerate(self.questions):
            tk.Label(omr_frame, text=f"{question}번").grid(row=i + 1, column=0, padx=10, pady=5)
            for j, option in enumerate(self.options):
                tk.Radiobutton(
                    omr_frame, text=option, variable=self.user_answers[question], value=option
                ).grid(row=i + 1, column=j + 1, padx=5)

        submit_button = tk.Button(omr_frame, text="제출", command=self.submit_answers)
        submit_button.grid(row=len(self.questions) + 1, column=0, columnspan=5, pady=10)

    def submit_answers(self):
        correct_count = sum(self.user_answers[question].get() == correct_answer
                            for question, correct_answer in zip(self.questions, self.correct_answers))
        if correct_count >= 3:
            messagebox.showinfo("Result", "정답입니다!")
            self.write_state(0)
        else:
            messagebox.showinfo("Result", "실패하셨습니다.")
            self.write_state(1)

        self.root.destroy()

    def write_state(self, state):
        with open('state.txt', 'w') as file:
            file.write(f'state=={state}')
