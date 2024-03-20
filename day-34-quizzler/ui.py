from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
FONT_NAME = "Arial"


class QuizUX:

    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = quiz

        #grid setup
        self.label = Label(text="Score: 0", fg=WHITE, bg=THEME_COLOR, font=(FONT_NAME, 10, "normal"))
        self.label.grid(row=0, column=1, pady=(0, 20))

        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=260, text=quiz.draw_question(),
                                                     anchor="center", font=(FONT_NAME, 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_icon = PhotoImage(file='images/true.png')
        self.true_label = Button(image=true_icon, highlightthickness=0,
                                 command=self.check_if_true)
        self.true_label.config(padx=20, pady=20)
        self.true_label.grid(row=2, column=0, pady=20)

        false_icon = PhotoImage(file='images/false.png')
        self.false_label = Button(image=false_icon, highlightthickness=0,
                                  command=self.check_if_false)
        self.false_label.grid(row=2, column=1, pady=20)

        self.window.mainloop()

    def flash_bg(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.reset_bg)

    def reset_bg(self):
        self.canvas.config(bg='white')
        self.window.after(10, self.update_ui)

    def check_if_true(self):
        self.flash_bg(self.quiz.check_answer(True))

    def check_if_false(self):
        self.flash_bg(self.quiz.check_answer(False))

    def update_ui(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.draw_question())
        else:
            self.canvas.itemconfig(self.question_text, text="Congratulations, you've reached the end :).")
            self.true_label.config(state='disabled')
            self.false_label.config(state='disabled')
        self.label.config(text=f"Score: {self.quiz.score}")

