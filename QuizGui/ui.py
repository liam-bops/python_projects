from tkinter import *
from quizbrain import QuizBrain
import html

BACK_COLOUR = '#1d3557'


class QuizUI:
    def __init__(self,quiz : QuizBrain):
        self.quizbrain = quiz
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=BACK_COLOUR)
        self.q_no = Label(bg=BACK_COLOUR, fg='white', text=f'Question : {self.quizbrain.question_number}', font=('Courier', 20),
                           pady=10, padx=10)
        self.score = Label(bg=BACK_COLOUR, fg='white', text=f'Score : {self.quizbrain.score}', font=('Courier', 20),
                           pady=10, padx=10)
        self.screen = Label(width=45, height=15, text=f'{self.quizbrain.question_text}',
                            font=('Courier', 20),wraplength= 500,justify='left')
        trueimg = PhotoImage(file='images/true.png')
        falseimg = PhotoImage(file='images/false.png')
        self.true_button = Button(padx=20, pady=20, image=trueimg,command=self.true_pressed)
        self.false_button = Button(padx=20, pady=20, image=falseimg,command=self.false_pressed)
        # self.true_button = Button(padx=20, pady=20)
        # self.false_button = Button(padx=20, pady=20)
        self.screen_setup()
        self.window.mainloop()

    def screen_setup(self):
        self.q_no.grid(row = 0,column= 0)
        self.score.grid(row=0, column=1)
        self.screen.grid(row=1, column=0, columnspan=2)
        # trueimg = PhotoImage(file='images/true.png')
        # falseimg = PhotoImage(file='images/false.png')
        # self.true_button = Button(padx=20, pady=20,image=trueimg)
        # self.false_button = Button(padx=20, pady=20,image=falseimg)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

    def next(self):
        self.score.config(text=f'Score : {self.quizbrain.score}')
        if self.quizbrain.is_over():
            self.screen.config(bg='white')
            self.screen.config(text="OUT OF QUESTIONS")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        else:
            self.quizbrain.next_question()
            self.screen.config(bg = 'white',text=f'{self.quizbrain.question_text}')
        self.q_no.config(text=f'Question : {self.quizbrain.question_number}')


    def false_pressed(self):
        is_right = self.quizbrain.check_answer('False')
        if is_right:
            self.screen.config(bg='green')
        else:
            self.screen.config(bg='red')
        self.window.after(1000,self.next)

    def true_pressed(self):
        is_right =self.quizbrain.check_answer('True')
        if is_right:
            self.screen.config(bg = 'green')
        else:
            self.screen.config(bg='red')
        self.window.after(1000,self.next)


