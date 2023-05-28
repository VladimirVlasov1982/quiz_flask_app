import datetime
from setup_db import db


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, unique=True)
    question_text = db.Column(db.String)
    answer_text = db.Column(db.String)
    created_at = db.Column(db.DateTime)

    def __init__(self, question_id: int, question_text: str, answer_text: str, created_at: datetime) -> None:
        self.question_id = question_id
        self.question_text = question_text,
        self.answer_text = answer_text,
        self.created_at = created_at

    def to_dict(self) -> dict:
        return {
            'question_id': self.question_id,
            'question_text': self.question_text,
            'answer_text': self.answer_text,
            'created_at': self.created_at.isoformat(),
        }
