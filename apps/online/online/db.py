# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from time import time

db = SQLAlchemy()

all_categories = (
        u"Дзіцячая пляцоўка",
        u"Кулінарны фестываль"
)
category_limit = 50

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.Unicode(100), nullable=False)
    message = db.Column(db.UnicodeText, nullable=False)
    created = db.Column(db.Integer(), nullable=False)

    def __init__(self, category, message):
        self.category   = category
        self.message    = message
        self.created    = int(time())

def message_dict(message):
    return {
            'category': message.category,
            'message': message.message,
            'created': message.created,
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
