import connection


def get_all_questions():
    return connection.read_questions()


def get_question(question_id):
    questions_list = connection.read_questions()
    for question in questions_list:
        if question['id'] == question_id:
            return question
    return 'The question does not exist.'


def get_answers(question_id):
    given_answers = []
    answers_list = connection.read_answers()
    for answer in answers_list:
        if answer['question_id'] == question_id:
            given_answers.append(answer)
    return given_answers
