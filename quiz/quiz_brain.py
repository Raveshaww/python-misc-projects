# ask the question
# check if the answer was right
# check if end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_choice = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        self.question_number += 1

        self.check_answer(user_choice, current_question)
        print(f"Current score: {self.score}/{self.question_number}\n\n")
    
    def still_has_questions(self):
        # will just return true if true, false if false. No If statement needed
        return self.question_number < len(self.question_list)

    def check_answer(self, user_choice, current_question):
        if user_choice.lower() == current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was {current_question.answer}")
