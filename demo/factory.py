# -*- coding: utf-8 -*-
from celery import Celery
from flask import Flask

from .ext import db, cache


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('demo.config')

    db.init_app(app)
    cache.init_app(app)

    return app


def create_celery_app(app=None):
    app = app or create_app()
    celery = Celery()
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
