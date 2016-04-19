from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import func

from app.models import db

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voted_on = db.Column(db.DateTime, default=func.now(), nullable=False)

    # Comment
    comment_id = db.Column(db.Integer, ForeignKey('comment.id'), nullable=False)
    value = db.Column(db.Integer, nullable=False)