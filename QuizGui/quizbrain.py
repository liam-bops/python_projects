import html


class QuizBrain:
    def __init__(self, questions:list):
        self.question = questions
        self.question_number = 0
        self.score = 0
        self.next_question()

    def next_question(self):
        self.current_question = self.question[self.question_number]['question']
        self.ans = self.question[self.question_number]['correct_answer']
        # print(self.current_question)
        # print(self.question[self.question_number]['correct_answer'])
        self.question_text = html.unescape(self.current_question)
        self.question_number += 1

    def is_over(self) -> bool:
        if self.question_number == len(self.question):
            return True
        else:
            return False

    def check_answer(self,user_answer):
        # print(f'user answwr  = {user_answer}')
        # print(f'actual answer = {self.ans}')
        if self.ans == user_answer:
            self.score +=1
            return True
        else:
            return False



