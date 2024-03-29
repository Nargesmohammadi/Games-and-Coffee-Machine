from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    print(question)
    question_next = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_next, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("you've completed the quiz.")
print(f"you're final score was {quiz.score}/{len(question_bank)}")