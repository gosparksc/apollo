from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models import db

class Question(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # Set to true when ready to publish
    # Should be after yes/no/maybe answers are generated
    is_live = db.Column(db.Boolean, default=False, nullable=False)

    posted_on = db.Column(db.DateTime, default=func.now(), nullable=False)
    title = db.Column(db.String(70), nullable=False)
    image_url = db.Column(db.String, nullable=False)

    # Used for routing
    url_string = db.Column(db.String, nullable=False)
    # Example "is-usc-healthy"
    # usc-apollo.org/questions/is-usc-healthy/

    # Allows us to access posts with question_instance.post
    posts = relationship('Post')
