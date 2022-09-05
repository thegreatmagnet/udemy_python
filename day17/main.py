from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(i['question'], i['correct_answer']) for i in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question() 

print(f'Final score {quiz.score} / {len(quiz.question_list)}')



