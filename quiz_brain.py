class quiz_brain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_score = 0
        self.q_list = q_list
    
    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current.questions} (True/False: )")
        self.check_answer(user_answer, current.answers)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.q_score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.q_score}/{self.q_number}")
        print("\n")
        