# -*- coding: utf-8 -*-
from flask_script import Manager

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


if __name__ == '__main__':
    manager.run()
