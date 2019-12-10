import connection

def sort_questions(order_key='submission_time', reversed=True):
    questions = connection.get_all_questions(convert_linebreaks=True)
    sorted_questions = sorted(questions, key = lambda i: i[order_key], reverse=reversed)
    return sorted_questions


