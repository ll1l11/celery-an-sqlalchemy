# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)
app.config.from_object('demo.config')


@app.route('/')
def index():
    return 'index'
