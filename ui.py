from tkinter import *
from quiz_brain import QuizBrain
import os

os.system('clear')

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg='White', highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=275,
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR
        )

        self.true_button_image = PhotoImage(file='images/true.png')
        self.false_button_image = PhotoImage(file='images/false.png')

        self.true_button = Button(
            image=self.true_button_image,
            highlightthickness=0,
            highlightbackground=THEME_COLOR,
            command=self.check_true
        )
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(
            image=self.false_button_image,
            highlightthickness=0,
            highlightbackground=THEME_COLOR,
            command=self.check_false
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='White')
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz!!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def check_true(self):
        self.give_feedback(self.quiz_brain.check_answer('True'))

    def check_false(self):
        self.give_feedback(self.quiz_brain.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='Green')
            self.quiz_brain.score += 1
            self.score_label.config(text=f'Score: {self.quiz_brain.score}')
        else:
            self.canvas.config(bg='Red')
        self.window.after(1000, self.get_next_question)
