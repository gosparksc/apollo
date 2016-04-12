import os

from flask import Flask, render_template

from app.models import db, Post, Question

def create_app():
    app = Flask(__name__)

    # Determine current environment
    env = os.environ.get('APOLLO_ENV').capitalize() if os.environ.get('APOLLO_ENV') else 'Development'
    app.config.from_object('config.'+ env)
    app.config['ENV'] = env

    # Are we using postgres specific features?
    assert 'postgres' in app.config['SQLALCHEMY_DATABASE_URI']

    # Set up api routes
    from app.controllers import question
    app.register_blueprint(question)

    # Set up template routes
    @app.route("/")
    def index():
        values = {}
        questions = Question.query.fitler(Question.is_live==True).all()
        values["questions"] = questions
        return render_template('index.html', **values)

    # Set up connection to DB
    db.init_app(app)
    return app