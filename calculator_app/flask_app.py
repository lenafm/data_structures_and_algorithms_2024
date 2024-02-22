from flask import Flask, render_template, request

app = Flask(__name__)  # create the instance of the flask class


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])  # associating the POST method with this route
def calculate():

    # using the request method from flask to request the values that were sent to the server through the POST method
    value1 = request.form['value1']
    value2 = request.form['value2']
    operation = str(request.form['operation'])

    # convert the input to floating points
    value1 = float(value1)
    value2 = float(value2)

    if operation == 'addition':
        return render_template('index.html', printed_result=str(value1 + value2))
    elif operation == 'substraction':
        return render_template('index.html', printed_result=str(value1 - value2))
    elif operation == 'multiplication':
        return render_template('index.html', printed_result=str(value1 * value2))
    elif operation == 'division':
        return render_template('index.html', printed_result=str(value1 / value2))
    else:
        return render_template('index.html', printed_result='Choose from either "addition", "substraction", "multiplication" or "division')

if __name__ == '__main__':
    app.run(debug=True)