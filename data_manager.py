import csv
import time
import connection

# It reads the content of the question.csv file


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
