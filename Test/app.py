import os
from http.client import responses

from flask import Flask

app = Flask(__name__)

@app.route('/hello/<username>')
def hello(username):
    return f"hello,{username}!"

@app.route('/even/<int:number>')
def even(number):
    if number % 2 == 0:
        result = 'чётное'
    else:
        result = "нечётное"

    return f"Число {number} <b>{result}</b>"

@app.route('/compare/<float:number_1>/<float:number_2>')
def compare(number_1, number_2):
    if number_1 == number_2:
        sign = "="
    elif number_1 > number_2:
        sign = ">"
    else:
        sign = "<"

    return f"<h3>Compare</h3>{number_1} {sign} {number_2}"

@app.route('/check_exists/<path:file_path>')
def check_exist(file_path):
    file_exists = os.path.exists(file_path)
    response_code = 200 if file_exists else 404
    result = "exists" if file_exists else "not exists"

    return f"File <h3>{file_path}</h3>{result}.", response_code

if __name__ == '__main__':
    app.run(debug=True)