#!/usr/bin/env python

from gevent import monkey
monkey.patch_all()

#import time
#from threading import Thread
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, close_room, disconnect
import json
import random

import logic

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
#thread = None

posts = logic.load_json('posts.txt')
users = logic.load_json('users.txt')
words = logic.words_set("static/wordlist.txt")

sentences = {u'226B79DB11270BA': {'sentence': [u'Can', u'you', u'complete'], u'upvotes': [], u'downvotes': []}}

def is_word(word):
    return word.lower() in words if word else None

def create_sentence():
    global posts
    global sentences
    temp = '{:015X}'.format(random.randrange(16**15))
    while temp in sentences or temp in posts:
        temp = '{:015X}'.format(random.randrange(16**15))
    else:
        new_id = temp
    sentences[new_id] = {'sentence': [], 'upvotes': [], 'downvotes': []}

def add_word(word, post_id):
    global sentences
    sentences[post_id]['sentence'].append(word)

def upvote(form_value):
    global posts
    post_id = form_value[6:]
    posts[post_id]['upvotes'].append(1)

def downvote(form_value):
    global posts
    post_id = form_value[6:]
    posts[post_id]['downvotes'].append(1)

def delete_sentence(post_id):
    global sentences
    del sentences[post_id]

def add_post(post_id):
    global posts
    global sentences
    posts[post_id] = sentences[post_id]
    with open("posts.txt", 'w') as posts_file:
        json.dump(posts, posts_file)

def inject_test_data():
    global posts
    posts = {'23B393D1150ACB4': {'sentence': ['A', 'short', 'sentence'], 'upvotes': [], 'downvotes': []}, '3030DBB2BE1D411': {'sentence': ['Another', 'sentence'], 'upvotes': [], 'downvotes': []}}

@app.route('/words')
def words_JSON():
    return jsonify({'words': sorted(words)})

@app.route('/posts')
def posts_JSON():
    if not posts:
        inject_test_data()
    return jsonify(posts)

@app.route('/', methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        if request.form.get('username'):
            session['name'] = request.form.get('username')
            return redirect(url_for('user', name=session['name']))
        else:
            return render_template('enter.html')
    else:
        return render_template('enter.html')

@app.route('/<name>', methods=['GET', 'POST'])
def user(name):
    return render_template('posts.html',
                            sentences=sentences,
                            name=name)

@app.route('/<name>/<sentence_id>', methods=['GET', 'POST'])
def sentence(name, sentence_id):
    if request.method == 'POST':
        if request.form.get('post'):
            add_post(sentence_id)
            delete_sentence(sentence_id)
            return redirect(url_for('user', name=name))
        elif request.form.get('upvote'):
            upvote(request.form.get('upvote'))
        elif request.form.get('downvote'):
            downvote(request.form.get('downvote'))
        elif is_word(request.form.get('word')):
            add_word(request.form.get('word'), sentence_id)
    return render_template('sentence.html',
                            sentences=sentences,
                            name=name,
                            id=sentence_id)

@socketio.on('my broadcast event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data']},
         broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Start your chat here'})

#if __name__ == '__main__':
#    socketio.run(app, host='0.0.0.0', port=8080)
