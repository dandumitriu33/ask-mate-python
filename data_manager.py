import connection

def sort_questions():
    questions = connection.get_all_questions(convert_linebreaks=True)
    sorted_questions = sorted(questions, key = lambda i: i['submission_time'], reverse=True)
    return sorted_questions


