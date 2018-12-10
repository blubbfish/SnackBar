from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine, create_engine

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

databaseName = 'CoffeeDB.db'
url = 'sqlite:///' + databaseName
engine = create_engine(url, connect_args={'check_same_thread': False}, poolclass=SingletonThreadPool)
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '123456790'
app.config['STATIC_FOLDER'] = 'static'
app.config['IMAGE_FOLDER'] = 'static/images'
app.config['ICON_FOLDER'] = 'static/icons'
app.config['DEBUG'] = False
app.config['SESSION_COOKIE_PATH'] = '/'

db = SQLAlchemy(app)