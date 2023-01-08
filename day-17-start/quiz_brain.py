
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(ans, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, ref):
        if answer.lower() == ref.lower():
            print('You got it right!')
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {ref}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print('\n')
