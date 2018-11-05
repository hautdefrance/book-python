from flask import json
from flask import Response
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/summary')
def summary():
    data = {'first_name': 'José', 'last_name': 'Jiménez'}
    return Response(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = ... # get post from Database by post_id
    return render_template('post.html', post=post)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
