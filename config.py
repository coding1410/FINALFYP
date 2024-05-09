from flask_sqlalchemy import SQLAlchemy  # import SQLAlchemy for database interactions

db = SQLAlchemy()  # create a new SQLAlchemy object

def init_app(app):
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # sets the secret key for the Flask app, used for session management and other security features
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # sets the database URI that should be used for the connection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # disable Flask-SQLAlchemy event system
    db.init_app(app)  # initializes app for use with this database setup

import os  # import os module to interact with the operating system

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')  # get the secret key from environment or use default
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')  # get the database URL from environment or use default
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # explicitly disable or enable track modifications
