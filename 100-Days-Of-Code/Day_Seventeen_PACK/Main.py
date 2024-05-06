from question_model import Question
from Data import question_data

for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        New_Question = Question(question_text,question_answer)