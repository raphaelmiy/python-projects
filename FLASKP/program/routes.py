from program import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/100days')
def p100Days():
    return render_template('100days.html')

@app.route('/practise')
def practise():
    return render_template('practise.html')