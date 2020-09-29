from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/health-check')
def health_check():
    return 'cool'    

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/todos')
def show_todos():
    return {
            "id": 1,
            "title": "Todo 1",
            "description": "Desc"
    }