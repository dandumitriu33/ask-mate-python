import connection


def generate_answer_id():
    answers_list = connection.read_answers()
    list_of_ids = []
    for answer in answers_list:
        list_of_ids.append(int(answer['id']))
    new_id = max(list_of_ids) + 1
    return new_id


def generate_question_id():
    question_list = connection.read_questions()
    list_of_ids = []
    for question in question_list:
        list_of_ids.append(int(question['id']))
    new_id = max(list_of_ids) + 1
    return new_id
