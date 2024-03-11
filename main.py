from data import question_data
from question_model import question
from quiz_brain import quiz_brain

question_bank = []
for questions in question_data:
    questions_text = questions['text']
    questions_answer = questions['answer']
    new_question = question(questions_text, questions_answer)
    question_bank.append(new_question)

quiz = quiz_brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.q_score}/{quiz.q_number}")