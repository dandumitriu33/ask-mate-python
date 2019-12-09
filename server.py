from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    return render_template('list.html')


@app.route('/add-question')
def add_question():
    return render_template('/add-question.html')


if __name__ == '__main__':
    app.run(debug=True)


