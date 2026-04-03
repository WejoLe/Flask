import datetime
import os
import random
import re

from flask import Flask

app = Flask(__name__)

cars = ['Chevrolet','Renault','Ford','Lada']
cats = ['Корниш-рекс','Русская голубая','Шотланская вислоухая','Мейн-кун','Манчкин']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, "war_and_peace.txt")

def get_words_from_book():
    """Возвращает список слов из книги без знаков препинания."""
    with open(BOOK_FILE, encoding='utf-8') as book:
        text = book.read()
    # Поиск слов на кириллице/латинице без пунктуации и цифр
    words = re.findall(r"[А-Яа-яЁёA-Za-z]+", text)
    return words

# Получаем список слов один раз при запуске программы
BOOK_WORDS = get_words_from_book()

visits = 0

@app.route('/hello_world')
def test_function():
    now = datetime.datetime.now().utcnow()
    return f'Привет, мир ! {now}'

@app.route('/cars')
def cars_function():
    return ', '.join(cars)

@app.route('/cats')
def cats_function():
    return random.choice(list(cats))

@app.route('/get_time/now')
def time_function():
    current_time = datetime.datetime.now()
    return f'Точное время: {current_time}'

@app.route('/get_time/future')
def time_now_after_hour():
    timedelta = datetime.timedelta (hours=1)
    current_time_after_hour = datetime.datetime.now() + timedelta
    return f'Точное время через час будет: {current_time_after_hour.time()}'

@app.route('/get_random_word')
def random_function():
    if not BOOK_WORDS:
        return 'Список слов пуст.'
    random_word = random.choice(BOOK_WORDS)
    return random_word

@app.route('/counter')
def counter():
    global visits
    visits += 1
    return str(visits)