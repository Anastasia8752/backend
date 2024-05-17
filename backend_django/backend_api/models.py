from django.db import models


class Question(models.Model):
    condition_text = models.TextField()
    type_answer = models.CharField(max_length=50, default='')
    answer_options = models.JSONField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    is_correct = models.BooleanField()


# Функция для добавления вопросов и ответов
def add_questions_and_answers():
    questions_and_answers = [
        {
            "condition_text": "Что такое алгоритм?",
            "type_answer": "text",
            "answer_options": [],
            "correct_answer": "Последовательность действий для решения задачи."
        },
        {
            "condition_text": "Что такое переменная в программировании?",
            "type_answer": "text",
            "answer_options": [],
            "correct_answer": "Символическое имя, связанное с некоторым местом в памяти, где хранится значение."
        },
        {
            "condition_text": "Как называется инструмент для отладки программ?",
            "type_answer": "text",
            "answer_options": [],
            "correct_answer": "Отладчик."
        }
    ]

    for question_data in questions_and_answers:
        question = Question.objects.create(
            condition_text=question_data["condition_text"],
            type_answer=question_data["type_answer"],
            answer_options=question_data["answer_options"]
        )
        Answer.objects.create(
            question=question,
            answer_text=question_data["correct_answer"],
            is_correct=True
        )
