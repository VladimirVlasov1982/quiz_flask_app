from setup_db import db
from app import app
import pytest
from models import Question

app.app_context().push()


@pytest.fixture
def client():
    return app.test_client()


def test_ask_question(client):
    # Проверяем, что при POST-запросе на /api/ask создается новый вопрос в базе данных

    response = client.post('/api/ask', json={'questions_num': 1})
    assert response.status_code == 200

    last_question = Question.query.order_by(Question.id.desc()).first()
    assert last_question is not None

    expected_response = {
        'question_id': last_question.question_id,
        'question_text': last_question.question_text,
        'answer_text': last_question.answer_text,
        'created_at': last_question.created_at.isoformat(),
    }
    assert response.json == expected_response
    db.session.delete(last_question)
    db.session.commit()
    db.session.close()
