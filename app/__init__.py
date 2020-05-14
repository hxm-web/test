
from flask import Flask
from flask_login import LoginManager

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象



from app import routes,models