# -*- coding: utf-8 -*-
from flask_script import Manager, Server

from demo import app
from demo.ext import db


manager = Manager(app)


@manager.command
def create_all():
    db.create_all()


@manager.command
def drop_all():
    db.drop_all()


@manager.command
def re_create_all():
    db.drop_all()
    db.create_all()


manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=8007)
)


if __name__ == '__main__':
    manager.run()
