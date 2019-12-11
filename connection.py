import csv
import os


DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'
DATA_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
DATA_HEADER_QUESTION = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
DATA_HEADER_ANSWER = ['id', 'submission_time', 'vote_number', 'question_id','message', 'image']


def read_answers():
    data_list = []
    with open('sample_data/answer.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append(dict(row))
    return data_list


def read_questions():
    data_list = []
    with open('sample_data/question.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append(dict(row))
    return data_list


def write_answers(data_list):
    with open('sample_data/answer.csv', 'w', newline='') as csvfile:
        fieldnames = DATA_HEADER_ANSWER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for answer in data_list:
            writer.writerow({'id': answer['id'],
                             'submission_time': answer['submission_time'],
                             'vote_number': answer['vote_number'],
                             'question_id': answer['question_id'],
                             'message': answer['message'],
                             'image': answer['image']
                             })


def write_questions(data_list):
    with open('sample_data/question.csv', 'w', newline='') as csvfile:
        fieldnames = DATA_HEADER_QUESTION
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for question in data_list:
            writer.writerow({'id': question['id'],
                             'submission_time': question['submission_time'],
                             'view_number': question['view_number'],
                             'vote_number': question['vote_number'],
                             'title': question['title'],
                             'message': question['message'],
                             'image': question['image']
                             })
