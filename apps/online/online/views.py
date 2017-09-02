# -*- coding: utf-8 -*-
from os import path
from flask import Blueprint, render_template, session, redirect, url_for, flash, jsonify, request, abort, send_from_directory, current_app
from PIL import Image

from .forms import LoginForm, MessageForm
from .utils import authorized_view, photos
from .db    import create_message, query_all_messages, message_dict, category_limit, query_categorized_messages, remove_message

views = Blueprint('views', __name__)

@views.route('/')
def index():
    try:
        if session['authorized']:
            return render_template('online/index_authorized.html', form=MessageForm())
    except KeyError:
        pass
    return render_template('online/index.html', form=LoginForm())

@views.route('/login', methods=[ 'POST' ])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['authorized'] = True
        return redirect(url_for('.index'))
    return render_template('online/index.html', form=form)

@views.route('/logout')
def logout():
    del session['authorized']
    return redirect(url_for('.index'))

@views.route('/messages', methods=[ 'POST' ])
@authorized_view
def post_messages():
    form = MessageForm()
    if form.validate_on_submit():
        photo = None
        if 'photo' in request.files and request.files['photo']:
            photo = photos.save(request.files['photo'])
        create_message(form.category.data, form.message.data, photo)
        flash(u"Дзякуй, паведамленне паспяхова атрымана", 'info')
        return redirect(url_for('.index'))
    flash(u"Выпраўце, калі ласка, адзначаныя памылкі і паспрабуйце наноў", "error")
    return render_template('online/index_authorized.html', form=form)

@views.route('/categorized-messages', methods=[ 'GET' ])
def get_categorized_messages():
    messages = query_categorized_messages()
    response = {}
    for message in map(message_dict, messages):
        category = message['category']
        try:
            response[category]['items'].append(message)
        except KeyError:
            response[category] = {'items': [message]}
        response[category]['category'] = category
        response[category]['category_limit'] = category_limit
    return jsonify({'messages': response})

@views.route('/messages', methods=[ 'GET' ])
def get_messages():
    offset = int(request.args['offset'])
    messages = query_all_messages(offset)
    next_offset = offset
    if messages.count() > 0:
        next_offset = next_offset + category_limit
    return jsonify({
        'messages': map(message_dict, messages),
        'next_offset': next_offset
    })

@views.route('/messages/<int:id>', methods=['DELETE'])
@authorized_view
def delete_message(id):
    remove_message(id)
    return ("", 200)

@views.route('/preset/list/<string:filename>', methods=['GET'])
def get_list_preset(filename):
    filepath = photos.path(filename)
    try:
        orig = Image.open(filepath)
    except IOError:
        abort(404)
    preset_path = path.join(path.dirname(__file__), current_app.static_folder, 'images', 'list', filename)
    if path.exists(preset_path):
        return send_from_directory(path.dirname(preset_path), filename)
    preset = orig.resize((int(orig.width*0.2), int(orig.height*0.2)))
    try:
        preset.save(preset_path)
    except IOError:
        abort(500)
    return send_from_directory(path.dirname(preset_path), filename)
