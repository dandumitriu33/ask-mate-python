import connection
import time
import util


def get_all_questions():
    return connection.read_questions()


def get_all_answers():
    return connection.read_answers()


def write_all_questions(data_list):
    connection.write_questions(data_list)


def write_all_answers(data_list):
    connection.write_answers(data_list)


def sort_questions(order_key='submission_time', reversed=True):
    questions = connection.read_questions()
    if order_key == 'view_number' or order_key == 'vote_number':
        sorted_questions = sorted(questions, key=lambda i: int(i[order_key]), reverse=reversed)
        return sorted_questions
    sorted_questions = sorted(questions, key = lambda i: i[order_key], reverse=reversed)
    return sorted_questions


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


def create_time():
    return int(time.time())


def create_new_line(question):
    new_line = {'id': util.generate_question_id(), 'submission_time': create_time(), 'view_number': 0, 'vote_number':  0,
                'title': question['title'], 'message': question['message'], 'image': ""}
    return new_line


def add_question_table(question):
    current_data = connection.read_questions()
    new_line = create_new_line(question)
    current_data.append(new_line)
    connection.write_questions(current_data)


def add_answer_to_file(answer, question_id):
    answer_dictionary = {}
    answer_dictionary['id'] = util.generate_answer_id()
    answer_dictionary['submission_time'] = create_time()
    answer_dictionary['vote_number'] = 0
    answer_dictionary['question_id'] = question_id
    answer_dictionary['message'] = answer
    answer_dictionary['image'] = ''
    answers_list = connection.read_answers()
    answers_list.append(answer_dictionary)
    connection.write_answers(answers_list)


