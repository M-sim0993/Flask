from flask import Flask

# Создаем объект приложения Flask
app = Flask(__name__)

# Определяем маршрут и привязываем его к функции
@app.route('/')
def hello():
    return "Hello, Flask!"

@app.route('/hello')
def hello_word():
    return "Hello, world!"

@app.route('/info')
def info():
    return "This is an informational page."

@app.route('/calc/<s1>/<s2>')
def calc(s1, s2):
    if is_number(s1) and is_number(s2):
        return f"The sum of {s1} and {s2} is {int(s1) + int(s2)}."
    else:
        return "Uncorrect data."

@app.route('/revers/<word>')
def revers(word):
    if len(word) > 0:
        return f"{word[::-1]}"
    else:
        return "Uncorrect data."

@app.route('/user/<name>/<int:age>')
def user_info(name, age):
    if len(name) > 0 and age > 0: 
        return f"Hello, {name}. You are {age} years old."
    else:
        return "Uncorrect data."

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Запуск приложения
if __name__ == "__main__":

    app.run(debug=True)

