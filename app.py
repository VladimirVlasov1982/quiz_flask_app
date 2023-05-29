from config import Config
from flask import request, jsonify
from functions import Function
from flask import Flask
from setup_db import db


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()


app = create_app(Config)
func = Function()


@app.route("/api/ask", methods=['POST'])
def ask_question():
    data = request.get_json()
    if "questions_num" not in data.keys():
        return {'error': 'Bad request'}, 400
    questions_num = data.get('questions_num')
    if type(questions_num) != int or int(questions_num) <= 0:
        return {'error': 'The question number should be a positive integer!'}, 400
    question_lst = []

    while questions_num > 0:
        question_data = func.get_question()
        question_id = question_data['id']

        if func.check_question(question_id):
            question = func.save_question_and_return(question_data)
            question_lst.append(question)
        else:
            continue
        questions_num -= 1

    last_question = question_lst[-1] if question_lst else []
    return jsonify(last_question.to_dict() if last_question else {}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
