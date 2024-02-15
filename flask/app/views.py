from .config import app
from flask import render_template, request


@app.route('/')
def home():
    context = {'title': 'Home', 'name': 'Bob'}
    return render_template('home.html', **context)


@app.route('/page')
def page():
    if request.args.get('oper') == '+':
        s = int(request.args.get('num')) + int(request.args.get('number'))
    elif request.args.get('oper') == '-':
        s = int(request.args.get('num')) - int(request.args.get('number'))
    elif request.args.get('oper') == '*':
        s = int(request.args.get('num')) * int(request.args.get('number'))
    elif request.args.get('oper') == '/':
        s = int(request.args.get('num')) / int(request.args.get('number'))
    else:
        s = 0
    return render_template('page.html', s=s)

# написати дві сторінки, одна має при заході питпти користувача ввести
# числа і ці числа додає в адресу посилання на другу сторінку
# при переході на другу сторінку виконати із цима числами додавання
