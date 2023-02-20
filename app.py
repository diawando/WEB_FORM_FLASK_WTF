from flask import Flask, render_template, redirect, url_for
from forms import CourseForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'm5\tt.\x02\xcf\x02\xd1\xac\x8e\x1f'


courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
}]

@app.route('/', methods=('GET', 'POST'))
def index():
    form = CourseForm()
    return render_template('index.html', form=form)