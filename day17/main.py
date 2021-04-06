from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    text1 = x["question"]
    answer1 = x["correct_answer"]
    new_quest = Question(text1, answer1)
    question_bank.append(new_quest)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your total score is {quiz.score}/{quiz.question_no}")