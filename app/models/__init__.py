from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from comment import Comment
from vote import Vote
from question import Question
from post import Post