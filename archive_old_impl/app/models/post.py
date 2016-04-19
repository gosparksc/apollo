from sqlalchemy import desc
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.schema import ForeignKey

from app.models import db, Comment, Question

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String, nullable=False)
    contents = db.Column(db.String, nullable=False)
    author_first = db.Column(db.String, nullable=False)
    author_last = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)

    # One of 'yes', 'no', or 'maybe'
    answer = db.Column(db.String, nullable=False)

    # Link to comments
    comments = relationship("Comment")

    # Link to question that post answers
    question_id = db.Column(db.Integer, ForeignKey('question.id'))
    question = relationship("Question", back_populates="posts")
