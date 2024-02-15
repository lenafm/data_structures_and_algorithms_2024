from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',
                           heading = 'My Heading')
@app.route('/hello/<city>')
def hello(city):
    return f"<h1>Hello, {city}</h1>"

