from flask import Flask
from flask import url_for
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test.html')


@app.route('/help/')
def help():
    return render_template('help.html')


@app.route('/old_help/')
def old_help():
    return '<b>HELP</b>' \
           '<p1>' \
           '<ul>' \
           '    <li> View help: URL/help </li>' \
           '    <li> Add: URL/add/__num1__/__num2__' \
           '    <li> View App accuracy URL/iris </li>' \
           '</ul>' \
           '</p1>' \
           '<br> We are adding features. Stay tuned..'


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    url_for('static', filename='style.css')
    return "Sum: %d" % (a + b) + ' !'


@app.route('/whoami/<username>')
def whoami(username):
    return "Hey, I'm %s. Like I didn't know earlier ;)" % username


@app.route('/test')
def test():
    return 'Testing!'


@app.route('/login')
def login():
    return 'Logging.. '


with app.test_request_context():
    print url_for('login')
    print url_for('test')
    print url_for('whoami', username='John Anderson')
    print url_for('add', a=142, b=354)

