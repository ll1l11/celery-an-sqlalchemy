# -*- coding: utf-8 -*-
from flask import abort
from demo.ext import db, cache


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    @classmethod
    @cache.memoize()
    def get(cls, ident):
        if ident is None:
            return
        item = cls.query.get(ident)
        if item is None:
            return
        db.session.expunge(item)
        return item

    @classmethod
    def get_or_404(cls, ident):
        item = cls.get(ident)
        if item is None:
            abort(404)
        return item

    @classmethod
    def delete_cache(cls, ident):
        cache.delete_memoized(cls.get, cls, ident)

    def save(self):
        db.session.add(self)
        item_id = getattr(self, 'id', None)
        if item_id:
            self.delete_cache(item_id)

    def __repr__(self):
        return 'User id:{0} name:{1}'.format(self.id, self.name)
