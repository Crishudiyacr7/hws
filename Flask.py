from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return f'The sum of {num1} and {num2} is {result}'
    else:
        return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)

