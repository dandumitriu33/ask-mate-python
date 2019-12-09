import csv
import time

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
