# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap

from demo.ext import db, cache
from demo import views


app = Flask(__name__)
app.config.from_object('demo.config')

db.init_app(app)
cache.init_app(app)
Bootstrap(app)

app.register_blueprint(views.bp)
