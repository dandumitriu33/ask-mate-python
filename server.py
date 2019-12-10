from flask import Flask, render_template, request, redirect, url_for
import connection
import data_manager


app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    questions = data_manager.sort_questions('submission_time', True)
    return render_template('list.html', questions=questions)


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

