from flask import Flask, render_template, request, redirect, url_for
import connection
import data_manager
app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    questions = data_manager.sort_questions('submission_time', True)
    return render_template('list.html', questions=questions)


if __name__ == '__main__':
    app.run(port=8000, debug=True)