import csv
import os
import time


DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'
DATA_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
DATA_HEADER_ANSWER = ['id', 'submission_time', 'vote_number', 'question_id','message', 'image']

def read_answers():
    data_list = []
    with open('sample_data/answer.csv', 'r', newline='') as csvfile:
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




# This function reads the CSV file

def get_data():
    data = []
    with open('./sample_data/question.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for items in csv_reader:
            data.append(items)
    return data

def write_data(new_data, fieldnames):
    with open('./sample_data/question.csv', 'w') as file:
        csv_write = csv.DictWriter(file, fieldnames=fieldnames)
        csv_write.writeheader()
        for line in new_data:
            csv_write.writerow({'id': line['id'], 'submission_time': line['submission_time'], 'view_number': line['view_number'],
                                 'vote_number': line['vote_number'], 'title': line['title'], 'message': line['message'], 'image': line['image']})


