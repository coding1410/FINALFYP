from config import db  # import the db instance from the config module

# define the Owner model to represent pet owners in the database
class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary key
    full_name = db.Column(db.String(100), nullable=False)  # owner's full name
    phone_number = db.Column(db.String(20), nullable=False)  # contact number
    email = db.Column(db.String(100), nullable=False)  # email address
    address = db.Column(db.String(200), nullable=False)  # home address
    pets = db.relationship('Pet', backref='owner', lazy=True)  # relationship to pets
    credentials = db.relationship('UserCredentials', backref='owner', uselist=False)  # link to credentials

# define the Pet model to represent pets owned by the owners
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary key
    name = db.Column(db.String(100), nullable=False)  # pet's name
    breed = db.Column(db.String(100), nullable=False)  # breed of the pet
    dob = db.Column(db.DateTime, nullable=False)  # date of birth
    primary_vet = db.Column(db.String(100), nullable=False)  # primary veterinarian
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)  # foreign key to owner

# define the UserCredentials model for storing login information linked to an owner
class UserCredentials(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary key
    username = db.Column(db.String(100), unique=True, nullable=False)  # username, must be unique
    password = db.Column(db.String(100), nullable=False)  # password
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)  # link to owner

from datetime import datetime  # import datetime for handling dates and times
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # create a new SQLAlchemy instance

# define the Product model for store products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary key
    name = db.Column(db.String(100), nullable=False)  # product name
    price = db.Column(db.Float, nullable=False)  # price
    description = db.Column(db.Text, nullable=True)  # optional description
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')  # image file with a default

# define the User model to store user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary key
    username = db.Column(db.String(20), unique=True, nullable=False)  # unique username
    email = db.Column(db.String(120), unique=True, nullable=False)  # unique email
    password = db.Column(db.String(60), nullable=False)  # hashed password
    # Additional fields can be added here

# define the Order model to store orders placed by users
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # foreign key to user
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # date the order was placed
    products = db.Column(db.PickleType, nullable=False)  # stores product IDs and quantities using a pickle type