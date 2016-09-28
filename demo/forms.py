# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from demo.ext import db
from demo.models import User


class UserForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    submit = SubmitField('Submit')

    def save(self, user=None):
        if not user:
            user = User()
        user.name = self.name.data

        user.save()
        db.session.commit()
        user = User.get(user.id)
        return user
