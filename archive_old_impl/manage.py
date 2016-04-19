from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask.ext.script import Command

from app import create_app
from app.models import db
from app.populate import populate

app = create_app()

class PopulateDB(Command):
    "Populates DB with fake data"
    def run(self):
        populate()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('populate', PopulateDB())

if __name__ == '__main__':
    manager.run()