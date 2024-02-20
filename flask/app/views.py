from .config import app
from flask import render_template, request, redirect
from .forms import RegistrationForm, LoginForm, File, PostForm


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


@app.route('/form', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        oper = request.form.get('operation')
        if oper == '+':
            s = num1 + num2
        elif oper == '-':
            s = num1 - num2
        elif oper == '*':
            s = num1 * num2
        elif oper == '/':
            s = num1 / num2
        else:
            s = 0
        return redirect(f'/res?res={s}')
    return render_template('form.html', title='Home')


@app.route('/res')
def result():
    return render_template('res.html', res=request.args.get('res'))


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.username.data
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        return render_template('login.html', form=form, name=name, password=password, remember_me=remember_me)
    return render_template('login.html', form=form)


@app.route('/file', methods=['GET', 'POST'])
def file():
    form = File()
    if form.validate_on_submit():
        file_data = form.file.data
        file_data.save(f'app/static/files/{file_data.filename}')
    return render_template('file.html', form=form)


@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        text = form.text.data
        image = form.image.data
        image.save(f'app/static/files/{image.filename}')
        return redirect(f'/post?path=/static/files/{image.filename}&text={text}')
    return render_template('create_post.html', form=form)


@app.route('/post')
def post_page():
    return render_template('post.html', text=request.args.get('text'), path=request.args.get('path'))
