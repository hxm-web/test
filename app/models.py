
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


from app import db
from datetime import datetime



class Comments(db.Model):
        __tablename__ = u'comments'
        id = db.Column(db.Integer, primary_key=True)
        content = db.Column(db.String(1000), nullable=False)
        timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)




