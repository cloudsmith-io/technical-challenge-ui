# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest
from flask_wtf.csrf import CSRFProtect
from passlib.context import CryptContext

csrf_protect = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()
flask_static_digest = FlaskStaticDigest()
login_manager = LoginManager()
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
