from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    posted_on = db.Column(db.DateTime, default=func.now(), nullable=False)
    contents = db.Column(db.String(5000), nullable=False)

    # Parent Post
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)

    #Upvotes
    votes = relationship("Vote")

    @property
    def num_upvotes(self):
        len([vote for vote in votes if vote.value == 1])

    @property
    def num_downvotes(self):
        len([vote for vote in votes if vote.value == -1])