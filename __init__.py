from flask import Flask, render_template, request, redirect, url_for, flash
from degrees_of_comparison import *
from search_words_on_letters import *
from segmentator_flexiy import *

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Секретний ключ для використання flash-повідомлень

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/task1', methods=['GET', 'POST'])
def task1():
    words = []
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            words = find_words(text)
        else:
            flash('Будь ласка, введіть текст!', 'error')
    return render_template('task1.html', words=words)

@app.route('/task2', methods=['GET', 'POST'])
def task2():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        degree = request.form.get('degree')
        if text and degree:
            result = process_adjectives(text, degree)
        else:
            flash('Будь ласка, введіть текст і виберіть ступінь порівняння', 'error')
    return render_template('task2.html', result=result)

@app.route('/task3', methods=['GET', 'POST'])
def task3():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        type = request.form.get('type')
        if type in ["Noun", "Adjective", "Verb"]:
            result = selector(text, type)
        else:
            flash('Будь ласка, введіть слова і виберіть частину мови', 'error')
    return render_template('task3.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

