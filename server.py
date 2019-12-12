from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
import os
import data_manager
import util

# at this time, the file reading method only supports the absolute path,
# which is subject to change, depending on the server running the software

UPLOAD_FOLDER = '/home/dan/codecool/web/w1/askmate/ask-mate-python/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
@app.route('/list', methods=['GET', 'POST'])
def route_list():
    if request.method == 'GET':
        sort_by = request.args.get(key='order_by')
        order_direction = request.args.get(key='order_direction')
        if sort_by == 'submission time' and order_direction == 'desc':
            questions = data_manager.sort_questions('submission_time', True)
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
        elif sort_by == 'submission time' and order_direction == 'asc':
            questions = data_manager.sort_questions('submission_time', False)
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
        elif sort_by == 'title' and order_direction == 'desc':
            questions = data_manager.sort_questions('title', True)
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
        elif sort_by == 'title' and order_direction == 'asc':
            questions = data_manager.sort_questions('title', False)
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
        elif sort_by == 'message' and order_direction == 'desc':
            questions = data_manager.sort_questions('message', True)
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
        elif sort_by == 'message' and order_direction == 'asc':
            questions = data_manager.sort_questions('message', False)
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
        elif sort_by == 'view number' and order_direction == 'desc':
            questions = data_manager.sort_questions('view_number', True)
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
        elif sort_by == 'view number' and order_direction == 'asc':
            questions = data_manager.sort_questions('view_number', False)
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
        elif sort_by == 'vote number' and order_direction == 'desc':
            questions = data_manager.sort_questions('vote_number', True)
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
        elif sort_by == 'vote number' and order_direction == 'asc':
            questions = data_manager.sort_questions('vote_number', False)
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
        else:
            questions = data_manager.get_all_questions()
            return render_template('list.html',
                                   category=sort_by,
                                   questions=questions)
    elif request.method == 'POST':
        file = request.files['file']
        new_question_id = util.generate_question_id()
        if file and allowed_file(file.filename):
            filename = "q" + str(new_question_id) + secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_question = {"id": new_question_id,
                        "submission_time": data_manager.create_time(),
                        "view_number": 0,
                        "vote_number": 0,
                        'title': request.form['title'],
                        'message': request.form['message'],
                        'image': '/static/img/' + filename if file.filename else ''}
        data_manager.add_question_table(new_question)
        questions = data_manager.get_all_questions()
        return render_template('/list.html',
                               questions=questions)


@app.route('/question/<question_id>/new-answer', methods=['GET'])
def new_answer(question_id):
    return render_template('new-answer.html',
                           question_id=question_id)


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def display_question(question_id):
    if request.method == 'GET':
        question = data_manager.get_question(question_id)
        answers = data_manager.get_answers(question_id)
        return render_template('question.html',
                               question=question,
                               answers=answers,
                               question_id=question_id)
    elif request.method == 'POST':
        file = request.files['file']
        new_answer_id = util.generate_answer_id()
        if file and allowed_file(file.filename):
            filename = 'a' + str(new_answer_id) + secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filename = '/static/img/' + filename
        data_manager.add_answer_to_file(request.form['post_answer'], question_id, new_answer_id, filename)
        question = data_manager.get_question(question_id)
        answers = data_manager.get_answers(question_id)
        return render_template('question.html',
                               question=question,
                               answers=answers,
                               question_id=question_id)


@app.route('/question/<question_id>/delete', methods=['GET'])
def delete_question(question_id):
    questions = data_manager.get_all_questions()
    i = 0
    while i < len(questions):
        if questions[i]['id'] == question_id:
            question_id = questions[i]['id']
            image_name = questions[i]['image']
            questions.pop(i)
        i += 1
    data_manager.write_all_questions(questions)
    answers = data_manager.get_all_answers()
    j = 0
    while j < len(answers):
        if answers[j]['question_id'] == question_id:
            answers.pop(j)
        j += 1
    data_manager.write_all_answers(answers)
    questions = data_manager.get_all_questions()
    complete_path = f"/home/dan/codecool/web/w1/askmate/ask-mate-python{image_name}"
    os.remove(complete_path)
    return render_template('list.html',
                           questions=questions)


@app.route('/question/<question_id>/edit', methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == 'GET':
        questions = data_manager.get_all_questions()
        i = 0
        while i < len(questions):
            if questions[i]['id'] == question_id:
                title = questions[i]['title']
                message = questions[i]['message']
            i += 1
        return render_template('edit_question.html',
                               title=title,
                               message=message,
                               question_id=question_id)
    elif request.method == 'POST':
        new_title = request.form['title']
        new_message = request.form['message']
        questions = data_manager.get_all_questions()
        i = 0
        while i < len(questions):
            if questions[i]['id'] == question_id:
                questions[i]['title'] = new_title
                questions[i]['message'] = new_message
            i += 1
        data_manager.write_all_questions(questions)
        question = data_manager.get_question(question_id)
        answers = data_manager.get_answers(question_id)
        return render_template('question.html',
                               question=question,
                               answers=answers,
                               question_id=question_id)


@app.route('/answer/<answer_id>/edit', methods=['GET', 'POST'])
def edit_answer(answer_id):
    if request.method == 'GET':
        answers = data_manager.get_all_answers()
        i = 0
        while i < len(answers):
            if answers[i]['id'] == answer_id:
                message = answers[i]['message']
            i += 1
        return render_template('edit_answer.html',
                               message=message,
                               answer_id=answer_id)
    elif request.method == 'POST':
        new_message = request.form['message']
        answers = data_manager.get_all_answers()
        i = 0
        while i < len(answers):
            if answers[i]['id'] == answer_id:
                question_id = answers[i]['question_id']
                answers[i]['message'] = new_message
            i += 1
        data_manager.write_all_answers(answers)
        question = data_manager.get_question(question_id)
        answers = data_manager.get_answers(question_id)
        return render_template('question.html',
                               question=question,
                               answers=answers,
                               question_id=question_id)


@app.route('/answer/<answer_id>/delete', methods=['GET'])
def delete_answer(answer_id):
    answers = data_manager.get_all_answers()
    i = 0
    while i < len(answers):
        if answers[i]['id'] == answer_id:
            question_id = answers[i]['question_id']
            image_name = answers[i]['image']
            answers.pop(i)
        i += 1
    data_manager.write_all_answers(answers)
    complete_path = f"/home/dan/codecool/web/w1/askmate/ask-mate-python{image_name}"
    os.remove(complete_path)
    question = data_manager.get_question(question_id)
    answers = data_manager.get_answers(question_id)
    return render_template('question.html',
                           question=question,
                           answers=answers,
                           question_id=question_id)


@app.route('/add-question')
def add_question():
    return render_template('/add-question.html')


@app.route('/question/<question_id>/vote_up')
def question_vote_up(question_id):
    questions = data_manager.get_all_questions()
    i = 0
    while i < len(questions):
        if questions[i]['id'] == question_id:
            questions[i]['vote_number'] = int(questions[i]['vote_number']) + 1
        i += 1
    data_manager.write_all_questions(questions)
    questions = data_manager.get_all_questions()
    return render_template('list.html', questions=questions)


@app.route('/question/<question_id>/vote_down')
def question_vote_down(question_id):
    questions = data_manager.get_all_questions()
    i = 0
    while i < len(questions):
        if questions[i]['id'] == question_id:
            questions[i]['vote_number'] = int(questions[i]['vote_number']) - 1
        i += 1
    data_manager.write_all_questions(questions)
    questions = data_manager.get_all_questions()
    return render_template('list.html', questions=questions)


@app.route('/answer/<answer_id>/vote_up')
def answer_vote_up(answer_id):
    answers = data_manager.get_all_answers()
    i = 0
    while i < len(answers):
        if answers[i]['id'] == answer_id:
            answers[i]['vote_number'] = int(answers[i]['vote_number']) + 1
            question_id = answers[i]['question_id']
        i += 1
    data_manager.write_all_answers(answers)
    question = data_manager.get_question(question_id)
    answers = data_manager.get_answers(question_id)
    return render_template('question.html',
                           question=question,
                           answers=answers,
                           question_id=question_id)


@app.route('/answer/<answer_id>/vote_down')
def answer_vote_down(answer_id):
    answers = data_manager.get_all_answers()
    i = 0
    while i < len(answers):
        if answers[i]['id'] == answer_id:
            answers[i]['vote_number'] = int(answers[i]['vote_number']) - 1
            question_id = answers[i]['question_id']
        i += 1
    data_manager.write_all_answers(answers)
    question = data_manager.get_question(question_id)
    answers = data_manager.get_answers(question_id)
    return render_template('question.html',
                           question=question,
                           answers=answers,
                           question_id=question_id)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run(debug=True)

