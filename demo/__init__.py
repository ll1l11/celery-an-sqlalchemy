# -*- coding: utf-8 -*-
from demo.factory import create_app

from demo import views

app = create_app()

app.register_blueprint(views.bp)
