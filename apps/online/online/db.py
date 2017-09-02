# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from time import time

from .utils import photos

db = SQLAlchemy()

all_categories = (
        u"Важныя абвесткі",
        u"Агульнае",
        u"Згублена-знойдзена",
        u"Сцэна",
        u"Турнірная пляцоўка",
        u"Пляцоўка ранняга сярэднявечча",
        u"Дзіцячая пляцоўка",
        u"Кулінарны фестываль",
        u"Рамесная слабада",
        u"Прыстань",
        u"Пляцоўка для стрэлаў з лукаў",
        u"Пляцоўка лятальных апаратаў",
        u"Кантактны заапарк",
        u"Майстар-класы",
        u"Фотазона",
        u"Лекторый",
)
category_limit = 50

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.Unicode(100), nullable=False)
    message = db.Column(db.UnicodeText, nullable=False)
    filename = db.Column(db.Unicode(200))
    created = db.Column(db.Integer(), nullable=False)

    def __init__(self, category, message, filename):
        self.category   = category
        self.message    = message
        self.created    = int(time())
        self.filename   = filename

def message_dict(message):
    return {
            'id': message.id,
            'category': message.category,
            'message': message.message,
            'created': message.created,
            'photo': '/preset/list/%s' % message.filename if message.filename != None else None,
            'photo_full': photos.url(message.filename),
    }

def create_message(*args):
    m = Message(*args)
    db.session.add(m)
    db.session.commit()

def query_categorized_messages():
    messages = []
    for category in all_categories:
        messages = messages + (
                Message.query.filter_by(category=category)
                             .order_by(Message.created.desc())
                             .limit(category_limit)
                             .all()
        )
    return messages

def query_all_messages(offset):
    return (
            Message.query.order_by(Message.created.desc())
                         .offset(offset)
                         .limit(category_limit)
    )

def remove_message(id):
    m = Message.query.get_or_404(id)
    db.session.delete(m)
    db.session.commit()
