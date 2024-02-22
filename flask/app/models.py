from .config import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


# String, Text, Integer, Float, Boolean, DateTime
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    age = db.Column(db.Integer)

    def password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(150), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    image = db.Column(db.String)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
# flask db migrate
# flask db upgrade
