from datetime import datetime
import requests
from requests.exceptions import RequestException
from setup_db import db
from models import Question


class Function:

    @staticmethod
    def get_question() -> dict:
        """
        Запрашиваем вопрос с сайта викторины
        """
        try:
            response = requests.get('https://jservice.io/api/random?count=1')
            question_data = response.json()[0]
            return question_data
        except RequestException as e:
            raise Exception({'status': 'error', 'message': str(e)})

    @staticmethod
    def check_question(question_id: int) -> bool:
        """
        Проверяем вопрос на наличие в базе.
        """
        question = Question.query.filter_by(question_id=question_id).first()
        return question == None

    @staticmethod
    def save_question_and_return(question_data: dict) -> Question:
        """
        Сохраняем вопрос в базе и возвращаем его
        """
        question_id = question_data['id']
        question_text = question_data['question']
        answer_text = question_data['answer']
        created_at = datetime.utcnow()

        question = Question(question_id, question_text, answer_text, created_at)
        db.session.add(question)
        db.session.commit()

        return question
