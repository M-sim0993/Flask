from app import app
from flask import render_template, request, redirect, url_for

# Определяем маршрут и привязываем его к функции
@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")  # Получаем имя из формы
        email = request.form.get("email")  # Получаем email из формы
        color = request.form.get("color")
        profession = request.form.get("profession")
        hobbies = request.form.getlist("hobbies")  # Для чекбоксов
        level = request.form.get("level")
        return render_template("result.html", name=name, email=email, color=color, profession=profession,
                               hobbies=hobbies, level=level)
    else:
        return redirect(url_for("form"))  # Если запрос GET, возвращаем на форму

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacts")
def contacts():
    return render_template("contact.html")

""" @app.route('/')
def hello():
    return "Hello, Flask!" """

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

@app.route('/user/<name>/<age>')
def user_info(name, age):
    if len(name) > 0 and age.isdigit(): 
        if int(age) > 0:
            return f"Hello, {name}. You are {age} years old."
        else:
            return "Uncorrect data."
    else:
        return "Uncorrect data."

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
