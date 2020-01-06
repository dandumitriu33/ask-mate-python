import connection
import datetime
import util


@connection.connection_handler
def get_all_questions(cursor, order_by='submission_time', order_direction='DESC'):
    order_dict = {
                'submission_time': "SELECT * FROM questions ORDER BY submission_time ",
                'title': "SELECT * FROM questions ORDER BY title ",
                'message': "SELECT * FROM questions ORDER BY message ",
                'view_number': "SELECT * FROM questions ORDER BY view_number ",
                'vote_number': "SELECT * FROM questions ORDER BY vote_number "
    }
    cursor.execute(order_dict[order_by] + order_direction + ";")
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def get_question(cursor, question_id):
    cursor.execute(f"""
                    UPDATE questions
                    SET view_number = view_number + 1
                    WHERE id = {question_id};
                    SELECT * FROM questions WHERE id = {question_id}; 
    """)
    question = cursor.fetchall()
    return question


@connection.connection_handler
def get_answers_for_question(cursor, question_id):
    cursor.execute(f"""
                    SELECT * FROM answers WHERE question_id = {question_id} ORDER BY vote_number DESC;
    """)
    answers = cursor.fetchall()
    return answers


@connection.connection_handler
def post_question(cursor, title, message, image=None):
    submission_time = datetime.datetime.utcnow().isoformat(' ', 'seconds')
    cursor.execute(f"""
                    INSERT INTO questions (submission_time, view_number, vote_number, title, message, image)
                    VALUES ('{submission_time}', 0, 0, '{title}', '{message}', '{image}');
""")
    cursor.execute(f"""
                    SELECT id FROM questions WHERE submission_time = '{submission_time}';
""")
    question_id = cursor.fetchall()[0]['id']
    return question_id


@connection.connection_handler
def delete_question(cursor, question_id):

    # deletes answers, then the question

    cursor.execute(f"""
                    DELETE FROM answers
                    WHERE question_id = {question_id};
                    DELETE FROM questions
                    WHERE id = {question_id};
    """)
