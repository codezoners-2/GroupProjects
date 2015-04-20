#!/usr/bin/env python

from flask import Flask, render_template, request
import json

app = Flask(__name__)

sentence = []
with open("posts.txt") as posts_file:
    posts = json.load(posts_file)

with open("wordlist.txt") as words_file:
    words = set(word.strip().lower() for word in words_file)

post_id = max(posts.keys()) if posts else 99999999

def add_1(old_id):
    return old_id + 1

def is_word(word):
    return word.lower() in words

def add_word(word):
    global sentence
    sentence.append(word)

def delete_sentence():
    global sentence
    sentence = []

def add_post():
    global posts
    global sentence
    posts[add_1(post_id)] = [' '.join(sentence), 0]
    with open("posts.txt", 'w') as posts_file:
        json.dump(posts, posts_file)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def word_sequence():
    if request.method == 'POST':
        if is_word(request.form.get('word')):
            add_word(request.form.get('word'))
        elif request.form.get('post'):
            add_post()
            delete_sentence()
        elif request.form.get('like'):
            
    else:
        delete_sentence()
    return render_template('silly_sentences.html',
                            sentence=sentence,
                            posts=posts)


app.run(host='0.0.0.0', port=8080, debug=True)
