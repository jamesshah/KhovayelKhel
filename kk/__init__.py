from kk import routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

app = Flask(__name__)

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['DEBUG'] = os.getenv('DEBUG')
app.config['PORT'] = os.getenv('PORT')
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_DEFAULT_SENDER=os.getenv('MAIL_USERNAME'),
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
)


db = SQLAlchemy(app)
mail = Mail(app)
