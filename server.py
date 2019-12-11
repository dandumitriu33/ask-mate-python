from flask import Flask, render_template, request, redirect
import data_manager


app = Flask(__name__)


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


@app.route('/question/<question_id>')
def display_question(question_id):
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

