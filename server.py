from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
import os
import data_manager
import util

# at this time, the file reading method only supports the absolute path,
# which is subject to change, depending on the server running the software

UPLOAD_FOLDER = '/home/dan/codecool/web/w1/askmate/ask-mate-python/static/img'
UPLOAD_FOLDER_IULIAN = '/home/iulian/PycharmProjects/ask-mate-python/static/img'
UPLOAD_FOLDER_DAN = '/home/dan/codecool/web/w1/askmate/ask-mate-python/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/', methods=['GET'])
def index():
    questions = data_manager.get_new_five_questions()
    return render_template('index.html',
                           questions=questions)


@app.route('/list')
def list_all_questions():
    order_by = 'submission_time'
    order_direction = 'DESC'
    if request.args.get(key='order_by'):
        order_by = request.args.get(key='order_by')
    if request.args.get(key='order_direction'):
        order_direction = request.args.get(key='order_direction')
    questions = data_manager.get_all_questions(order_by, order_direction)
    return render_template('list.html',
                           questions=questions)


@app.route('/question/<question_id>')
def display_question(question_id):
    question_id = int(question_id)
    question = data_manager.get_question(question_id)
    answers = data_manager.get_answers_for_question(question_id)
    answer_id_list = []
    for answer in answers:
        answer_id_list.append(str(answer['id']))
    # answer_id_set = set(answer_id_list)
    comments = data_manager.get_comments_for_question_page(question_id, answer_id_list)
    return render_template('question.html',
                           question_id=question_id,
                           question=question,
                           comments=comments,
                           answers=answers)


@app.route('/add-question', methods=['GET', 'POST'])
def new_question():
    if request.method == 'GET':
        return render_template('add_question.html')
    elif request.method == 'POST':
        new_question_title = request.form['title'].replace("'", "''")
        new_question_message = request.form['message'].replace("'", "''")
        question_id = data_manager.post_question(new_question_title, new_question_message)
        question = data_manager.get_question(question_id)
        answers = data_manager.get_answers_for_question(question_id)
        return render_template('question.html',
                               question_id=question_id,
                               question=question,
                               answers=answers)


# TODO: remove files from answers when the question is deleted
@app.route('/question/<question_id>/delete')
def delete_question(question_id):
    data_manager.delete_question(question_id)
    return redirect(url_for('list_all_questions'))


@app.route('/question/<question_id>/edit', methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == 'GET':
        question = data_manager.get_question(question_id)
        return render_template('edit_question.html',
                               question_id=question_id,
                               question=question)
    elif request.method == 'POST':
        edited_question_title = request.form['title'].replace("'", "''")
        edited_question_message = request.form['message'].replace("'", "''")
        data_manager.update_question(question_id, edited_question_title, edited_question_message)
        return redirect(url_for('display_question', question_id=question_id))


@app.route('/question/<question_id>/new-comment', methods=['GET', 'POST'])
def question_new_comment(question_id):
    if request.method == 'GET':
        return render_template('new_comment.html', question_id=question_id)
    elif request.method == 'POST':
        new_comment_message = request.form['message'].replace("'", "''")
        data_manager.post_comment_question(question_id, new_comment_message)
        return redirect(url_for('display_question', question_id=question_id))


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def question_new_answer(question_id):
    if request.method == 'GET':
        return render_template('new_answer.html',
                               question_id=question_id)
    elif request.method == 'POST':
        new_answer_message = request.form['message'].replace("'", "''")
        data_manager.post_answer(question_id, new_answer_message)
        return redirect(url_for('display_question', question_id=question_id))


@app.route('/answer/<answer_id>/new-comment', methods=['GET', 'POST'])
def answer_new_comment(answer_id):
    if request.method == 'GET':
        return render_template('new_comment.html', answer_id=answer_id)
    elif request.method == 'POST':
        new_comment_mesage = request.form['message'].replace("'", "''")
        data_manager.post_comment_answer(answer_id, new_comment_mesage)
        question_id = data_manager.get_answer_question_id(answer_id)
        return redirect(url_for('display_question', question_id=question_id))


@app.route('/comment/<comment_id>/edit', methods=['GET', 'POST'])
def edit_comment(comment_id):
    if request.method == 'GET':
        comment = data_manager.get_comment(comment_id)
        return render_template('edit-comment.html',
                               comment_id=comment_id,
                               comment=comment)
    elif request.method == 'POST':
        comment = data_manager.get_comment(comment_id)
        if comment[0]['question_id']:
            question_id = comment[0]['question_id']
            edited_comment_message = request.form['message'].replace("'", "''")
            data_manager.update_comment(comment_id, edited_comment_message)
            return redirect(url_for('display_question',
                                    question_id=question_id))
        elif comment[0]['answer_id']:
            answer_id = comment[0]['answer_id']
            edited_comment_message = request.form['message'].replace("'", "''")
            data_manager.update_comment(comment_id, edited_comment_message)
            answer = data_manager.get_answer(answer_id)
            question_id = answer['question_id']
            return redirect(url_for('display_question',
                                    question_id=question_id))


@app.route('/answer/<answer_id>/edit', methods=['GET', 'POST'])
def edit_answer(answer_id):
    if request.method == 'GET':
        answer = data_manager.get_answer(answer_id)
        return render_template('edit_answer.html',
                               answer_id=answer_id,
                               answer=answer)
    elif request.method == 'POST':
        answer = data_manager.get_answer(answer_id)
        question_id = answer['question_id']
        edited_answer_message = request.form['message'].replace("'", "''")
        data_manager.update_answer(answer_id, edited_answer_message)
        return redirect(url_for('display_question',
                                question_id=question_id))


@app.route('/answer/<answer_id>/delete')
def delete_answer(answer_id):
    answer = data_manager.get_answer(answer_id)
    question_id = answer['question_id']
    data_manager.delete_answer(answer_id)
    return redirect(url_for('display_question',
                            question_id=question_id))


@app.route('/add-question')
def add_question():
    return render_template('/add_question.html')


@app.route('/question/<question_id>/vote-up')
def question_vote_up(question_id):
    data_manager.question_vote_up(question_id)
    return redirect(url_for('display_question',
                            question_id=question_id))


@app.route('/question/<question_id>/vote-down')
def question_vote_down(question_id):
    data_manager.question_vote_down(question_id)
    return redirect(url_for('display_question',
                            question_id=question_id))


@app.route('/answer/<answer_id>/vote-up')
def answer_vote_up(answer_id):
    data_manager.answer_vote_up(answer_id)
    answer = data_manager.get_answer(answer_id)
    question_id = answer['question_id']
    return redirect(url_for('display_question',
                            question_id=question_id))


@app.route('/answer/<answer_id>/vote-down')
def answer_vote_down(answer_id):
    data_manager.answer_vote_down(answer_id)
    answer = data_manager.get_answer(answer_id)
    question_id = answer['question_id']
    return redirect(url_for('display_question',
                            question_id=question_id))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run(debug=True,
            host='localhost')

