from .config import app, login
from flask import render_template, request, redirect
from .forms import RegistrationForm, LoginForm, PostForm
from .models import User, db, Post
from sqlalchemy.exc import IntegrityError
from flask_login import current_user, login_user, logout_user


@login.user_loader
def user_loader(id):
    return User.query.get(id)


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
        password = form.password.data
        email = form.email.data
        age = form.age.data
        user = User(username=name, email=email, age=age)
        user.password_hash(password)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        except IntegrityError:
            db.session.rollback()
            return render_template('registration.html', form=form, msg=1)
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        user = User.qury.filter_by(username=name).first()
        if not user or not user.check_password(password):
            return render_template('login.html', form=form, msg=1)
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')


@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        image = form.image.data
        if image.filename == '':
            post = Post(title=title, text=text, user=1)
            db.session.add(post)
            db.session.commit()
        else:
            image.save(f'app/static/files/{image.filename}')
            post = Post(title=title, text=text, user=1, image=f'/static/files/{image.filename}')
            db.session.add(post)
            db.session.commit()
        return redirect('/')
    return render_template('create_post.html', form=form)


@app.route('/post')
def post_page():
    return render_template('post.html', text=request.args.get('text'), path=request.args.get('path'))
