#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return string

@app.route("/count/<int:parameter>")
def count(parameter):
    result = '\n'.join(str(i) for i in range(parameter + 1)) + '\n'  # Add 1 to include the upper bound and a newline at the end
    return result

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        if num2 != 0:
            return str(num1 / num2)
        else:
            return "Cannot divide by zero"
    elif operation == "%":
        return str(num1 % num2)
    else:
        return "Invalid operation"
if __name__ == '__main__':
    app.run(port=5555, debug=True)

