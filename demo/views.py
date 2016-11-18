# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Blueprint, render_template, jsonify, redirect, url_for
from flask.views import MethodView

from demo.ext import db
from demo.models import User
from demo.forms import UserForm
from demo import tasks

bp = Blueprint('user', __name__)


class IndexView(MethodView):

    def get(self):
        result = db.session.query(User.id).order_by(User.id.desc()).first()
        if not result:
            url = url_for('.add')
            return redirect(url)
        user_id, = result
        user = User.get(user_id)
        return render_template('index.html', user=user)


class UserView(MethodView):
    def get(self, user_id):
        """编辑页面"""
        user = User.get_or_404(user_id)
        form = UserForm(obj=user)
        return render_template('user-edit.html', form=form, user=user)

    def post(self, user_id):
        user = User.get_or_404(user_id)
        form = UserForm()
        if form.validate():
            u = form.save(user)
            return str(u)
        else:
            return jsonify(errors=form.errors)


class AddView(MethodView):
    def get(self):
        form = UserForm()
        return render_template('user-add.html', form=form)

    def post(self):
        form = UserForm()
        if form.validate():
            u = form.save()
            return str(u)
        else:
            return jsonify(errors=form.errors)


class TestView(MethodView):
    def get(self):
        u = User.query.get(1)
        print(db.session)
        u.name = datetime.now().strftime('%H-%M-%S-%f')
        u.save()
        # print('views: ', db.session)
        tasks.send_mail()

        # print(u in db.session)
        # # u.name = '1234'
        db.session.commit()
        # data = str(u)
        # return data
        return '123'


bp.add_url_rule('/', view_func=IndexView.as_view('index'))
bp.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('user'))
bp.add_url_rule('/add', view_func=AddView.as_view('add'))
bp.add_url_rule('/test', view_func=TestView.as_view('test'))
