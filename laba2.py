from flask import Flask, render_template, request, flash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Секретний ключ для використання flash-повідомлень

# --- Перша задача: пошук слів на "і" та "и" ---

def find_words(text):
    words = re.findall(r'\b[іиІИ][\w]{2,}', text)
    return words

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

# --- Друга задача: утворення вищого та найвищого ступенів прикметників (проста форма) ---

# Список прикметників, які не утворюють ступенів порівняння
ungradable_adjectives = {
    'нім', 'сліп', 'лис', 'мертв', 'жонат',
    'ворон', 'гнід', 'булан', 'чал',
    'вишнев', 'буряков', 'персиков',
    'превелик', 'завелик', 'маленьк', 
    'чорнесеньк', 'здоровенн', 'старезн', 
    'загребущ', 'чорняв', 'жовтуват', 'синюват',
    'білокрил', 'гостроок', 'прудконог'
}

def comparative_adjective(word: str) -> str:
    word = word.casefold()

    #винятки
    irregulars = {
        'гарн': 'кращ',
        'поган': 'гірш',
        'велик': 'більш',
        'висок' : 'вищ',
        'товст' : 'товщ',
        'низьк' : 'нижч',
        'вузьк' : 'вужч',
        'близьк' : 'ближч',
        'дуж' : 'дужч',
        'дорог' : 'дорожч',
    }

   
    base_pattern = r"(\w+)(ий|а|е|і)$"
    match = re.match(base_pattern, word)
    
    if match:
        base = match.group(1)
        ending = match.group(2)

        # Перевірка, чи належить основа до незмінних прикметників
        if base in ungradable_adjectives:
            return f"{word} - не утворює ступенів порівняння"

        # Вищий простий ступінь
        if base in irregulars.keys():
            return f"{irregulars[base]}{ending}"
        elif base in ['тяжк', 'важк']:
            return f"{base[:-1]}ч{ending}"
        elif base.endswith('к'):
            return f"{base[:-1]}ш{ending}"
        elif base.endswith(('ок', 'ек')):
            return f"{base[:-2]}ш{ending}"

        return f"{base}іш{ending}"
    
    return f"{word} - не є прикметником"

def superlative_adjective(word: str) -> str:
    word = word.casefold()
 
    base_pattern = r"(\w+)(ий|а|е|і)$"
    match = re.match(base_pattern, word)

    if match:
      base = match.group(1)
      if base in ungradable_adjectives:
        return f"{word} - не утворює ступенів порівняння"
        # Простий найвищий ступінь
      return f"най{comparative_adjective(word)}"
    
    return f"{word} - не є прикметником"
    
def process_adjectives(text: str, degree: str) -> str:
    words = text.split()
    result = []
    

    if degree == "comparative":
      for word in words:
         result.append(comparative_adjective(word))
    elif degree == "superlative":
      for word in words:
         result.append(superlative_adjective(word))
    else:
      return "Некоректний ступінь порівняння"

    return " ".join(result)

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

if __name__ == '__main__':
    app.run(debug=True)
