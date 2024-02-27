from .config import app, login
from flask import render_template, request, redirect
from .forms import RegistrationForm, LoginForm, PostForm, CommentForm
from .models import User, db, Post, Comment, Like
from sqlalchemy.exc import IntegrityError
from flask_login import current_user, login_user, logout_user, login_required


@login.user_loader
def user_loader(id):
    return User.query.get(id)


@app.route('/')
def home():
    if request.args:
        posts = Post.query.all().order_by(request.args.get('col'))
    else:
        posts = Post.query.all()
    context = {'title': 'Home', 'user': current_user, 'posts': posts}
    return render_template('home.html', **context)


@app.route('/posts/<int:id>', methods=['GET', 'POST'])
def post_page(id):
    form = CommentForm()
    post = Post.query.get(id)
    likes = Like.query.filter_by(post=id)
    is_liked = False
    for l in likes:
        if current_user == User.query.get(l.user):
            is_liked = True
            break
    if request.method == 'POST':
        if len(request.form.keys()) == 2:
            comment = Comment(text=form.text.data, post=id, user=current_user.id)
            db.session.add(comment)
            db.session.commit()
            return {'data': f'<p>{form.text.data}</p>'}
        else:
            for l in likes:
                if current_user == User.query.get(l.user):
                    db.session.delete(l)
                    db.session.commit()
                    return {'liked': False, 'amount': len(likes) - 1}
            else:
                l = Like(user=current_user.id, post=id)
                db.session.add(l)
                db.session.commit()
                return {'liked': True, 'amount': len(likes) + 1}
    comments = Comment.query.filter_by(post=id)
    return render_template('post_page.html', post=post, form=form, comments=comments, liked=is_liked, amount=len(likes))


# @app.route('/create_comment<int:id>', methods=['GET', 'POST'])
# def create_comment(id):
#     form = CommentForm()
#     if form.validate_on_submit():
#         comment = Comment(text=form.text.data, post=id, user=current_user.id)
#         db.session.add(comment)
#         db.session.commit()
#     return redirect(f'/posts/{id}')


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


@app.route('/form/', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        print(request.form)
        # print(request.json)
        # print(request.is_json)
        return {'a': 100}
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
        user = User.query.filter_by(username=name).first()
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
@login_required
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
            post = Post(title=title, text=text, user=current_user.id, image=f'/static/files/{image.filename}')
            db.session.add(post)
            db.session.commit()
        return redirect('/')
    return render_template('create_post.html', form=form)
