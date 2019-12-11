from flask import Flask, render_template, request, redirect
import data_manager
import connection


app = Flask(__name__)

LAST_VISITED_QUESTION = 0


@app.route('/')
@app.route('/list')
def route_list():
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
        questions = data_manager.get_data()
        return render_template('list.html',
                               category=sort_by,
                               questions=questions)


@app.route('/question/<question_id>/new-answer', methods=['GET'])
def new_answer(question_id):
    return render_template('new-answer.html',
                           question_id=question_id)


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def display_question(question_id):
    global LAST_VISITED_QUESTION
    if request.method == 'GET':
        question = data_manager.get_question(question_id)
        answers = data_manager.get_answers(question_id)
        LAST_VISITED_QUESTION = question_id
        return render_template('question.html',
                               question=question,
                               answers=answers,
                               question_id=question_id)
    elif request.method == 'POST':
        data_manager.add_answer_to_file(request.form['post_answer'], question_id)
        question = data_manager.get_question(question_id)
        answers = data_manager.get_answers(question_id)
        LAST_VISITED_QUESTION = question_id
        return render_template('question.html',
                               question=question,
                               answers=answers,
                               question_id=question_id)


@app.route('/question/<question_id>/edit', methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == 'GET':
        questions = data_manager.get_data()
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
        questions = data_manager.get_data()
        i = 0
        while i < len(questions):
            if questions[i]['id'] == question_id:
                questions[i]['title'] = new_title
                questions[i]['message'] = new_message
            i += 1
        connection.write_data(questions,
                              ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image'])
        question = data_manager.get_question(question_id)
        answers = data_manager.get_answers(question_id)
        return render_template('question.html',
                               question=question,
                               answers=answers,
                               question_id=question_id)


@app.route('/answer/<answer_id>/delete', methods=['GET'])
def delete_answer(answer_id):
    answers = connection.read_answers()
    i = 0
    while i < len(answers):
        if answers[i]['id'] == answer_id:
            question_id = answers[i]['question_id']
            answers.pop(i)
        i += 1
    connection.write_answers(answers)
    question = data_manager.get_question(question_id)
    answers = data_manager.get_answers(question_id)
    return render_template('question.html',
                           question=question,
                           answers=answers,
                           question_id=question_id)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        new_data = request.form
        data_manager.add_question_table(new_data)
        return redirect('/')
    else:
        return render_template('/add-question.html')


if __name__ == '__main__':
    app.run(debug=True)

