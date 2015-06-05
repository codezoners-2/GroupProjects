#!/usr/bin/env python
from gevent import monkey
monkey.patch_all()

#import time
#from threading import Thread
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, close_room, disconnect

from logic import *

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
#thread = None

posts = load_json('posts.txt')
users = load_json('users.txt')
words = words_set("static/wordlist.txt")
sentences = {}
sentences.update(inject_test_sentences())

@app.route('/', methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        if request.form.get('username'):
            user = request.form.get('username')
            if user not in users:
                add_user(users, user)
            session['name'] = user
            return redirect(url_for('user', name=session['name']))
        else:
            return render_template('enter.html')
    else:
        return render_template('enter.html')

@app.route('/<name>', methods=['GET', 'POST'])
def user(name):
    if request.form.get('upvote'):
        upvote(posts, users, name, request.form.get('upvote'))
    elif request.form.get('downvote'):
        downvote(posts, users, name, request.form.get('downvote'))
    return render_template('posts.html',
                            sentences=sentences,
                            name=name)

@app.route('/<name>/<sentence_id>', methods=['GET', 'POST'])
def sentence(name, sentence_id):
    if request.method == 'POST':
        if request.form.get('post'):
            add_post(posts, sentences, sentence_id)
            delete_sentence(sentences, sentence_id)
            return redirect(url_for('user', name=name))
        elif request.form.get('upvote'):
            upvote(posts, users, name, request.form.get('upvote'))
        elif request.form.get('downvote'):
            downvote(posts, users, name, request.form.get('downvote'))
        elif is_word(words, request.form.get('word')):
            add_word(sentences, request.form.get('word'), sentence_id)
    return render_template('sentence.html',
                            sentences=sentences,
                            name=name,
                            id=sentence_id,
                            users=users.keys())

@app.route('/words')
def words_JSON():
    return jsonify({'words': sorted(words)})

@app.route('/posts')
def posts_JSON():
    if not posts:
        return jsonify(inject_test_posts(posts))
    else:
        return jsonify(posts)

#- @app.route('/posts/<int:counter>')
#- def posts_JSON(counter):
    #- return jsonify(posts)

@socketio.on('my broadcast event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Start your chat here'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)
