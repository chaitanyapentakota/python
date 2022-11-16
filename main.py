from question_model import Question
from data import DATA
from quiz_game import Quiz_game

question_bank=[]
for question in DATA:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz= Quiz_game(question_bank)
while quiz.still_have_questions():
    quiz.next_question()