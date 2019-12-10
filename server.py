from flask import Flask, render_template, request, redirect, url_for
import data_manager
app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    return render_template('list.html')


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


