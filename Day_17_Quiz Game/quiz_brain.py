



#Attributes = question_number = 0, question_list = initialized when playing the game. Uses the question_bank

class QuizBrain:

    # TODO 1 = Asking questions
    def __init__(self, question_lst):
        self.question_number = 0
        self.question_list = question_lst
        self.answer_score = 0 #Dit is feitelijk niet nodig, je kunt een attributie doen in het object zelf.


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (true or false) ")
        self.check_answer(user_answer, current_question.answer)


    # TODO 3 = Checking if we are at the end of the game

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # TODO 2 = Checking if the answer was correct

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.answer_score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.answer_score} / {self.question_number}")
        print("\n")

    #TODO 4: Keep score



