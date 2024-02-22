from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',
                           heading = 'My Heading')
@app.route('/hello/<city>')
def hello(city):
    return f"<h1>Hello, {city}</h1>"

@app.route('/about')
def about():
    return render_template('about.html')

