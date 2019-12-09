import csv


def read_questions():
    data_list = []
    with open('sample_data/question.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append(dict(row))
    return data_list


def read_answers():
    data_list = []
    with open('sample_data/answer.csv', 'r',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append(dict(row))
    return data_list
