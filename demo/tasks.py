# -*- coding: utf-8 -*-
from .factory import create_celery_app
from .models import User
from .ext import db

celery = create_celery_app()


# @celery.task
def send_mail():
    # User.query.get(1)
    # print(db.session)
    print('#' * 20)
