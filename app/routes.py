from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Franklin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Suan'},
            'body': "The avengers movie was so coll!"
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts) 