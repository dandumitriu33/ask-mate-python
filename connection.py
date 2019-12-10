import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'
DATA_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

def get_all_questions(convert_linebreaks=False):
    all_questions = get_csv_data()

    if convert_linebreaks:
        for question in all_questions:
            #  allow multiline strings to display in HTML
            question['title'] = convert_linebreaks_to_br(question['title'])
            question['message'] = convert_linebreaks_to_br(question['message'])

    return all_questions

def get_csv_data(one_question_id=None):
    questions = []
    with open(DATA_FILE_PATH) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            question = dict(row)
            if one_question_id is not None and one_question_id == question['id']:
                return question
            questions.append(question)
    return questions

def convert_linebreaks_to_br(original_str):
    return '<br>'.join(original_str.split('\n'))

