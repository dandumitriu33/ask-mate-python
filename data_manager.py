import connection
import time
import util


def sort_questions(order_key='submission_time', reversed=True):
    questions = connection.get_data()
    sorted_questions = sorted(questions, key = lambda i: i[order_key], reverse=reversed)
    return sorted_questions


def get_question(question_id):
    questions_list = connection.get_data()
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


def get_data():
    return connection.get_data()


def create_id(data):
    return len(data)


def create_time():
    return int(time.time())


def create_new_line(question):
    new_line = {'id': create_id(get_data()), 'submission_time': create_time(), 'view_number': 0, 'vote_number':  0,
                'title': question['title'], 'message': question['message'], 'image': ''}
    return new_line


def add_question_table(question):
    current_data = get_data()
    new_line = create_new_line(question)
    current_data.append(new_line)
    for dic in current_data:
        fieldnames = [*dic]
        break

    connection.write_data(current_data, fieldnames)


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


