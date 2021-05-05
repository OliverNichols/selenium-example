from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SECRET_KEY=secrets.token_hex(8)
)

db = SQLAlchemy(app)

from application import routes