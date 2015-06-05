#!/usr/bin/env python
import json
import random

def load_json(json_file):
    with open(json_file) as the_file:
        return json.load(the_file)

def words_set(wordlist):
    with open(wordlist) as words_file:
        return set(word.strip().lower() for word in words_file if word.strip())

def is_word(words, word):
    return word.lower() in words if word else None

def create_sentence(posts, sentences):
    temp = '{:015X}'.format(random.randrange(16**15))
    while temp in sentences or temp in posts:
        temp = '{:015X}'.format(random.randrange(16**15))
    else:
        new_id = temp
    sentences[new_id] = {'sentence': [], 'upvotes': [], 'downvotes': []}

def add_word(sentences, word, post_id):
    sentences[post_id]['sentence'].append(word)

def delete_sentence(sentences, post_id):
    del sentences[post_id]

def add_post(posts, sentences, post_id):
    posts[post_id] = sentences[post_id]
    with open("posts.txt", 'w') as posts_file:
        json.dump(posts, posts_file)

def add_user(users, name):
    users[name] = {u'upvotes': [], u'downvotes': []}
    with open("users.txt", 'w') as users_file:
        json.dump(users, users_file)

def upvote(posts, users, user, post_id):
    post_id = str(post_id[6:])
    if user not in posts[post_id][u'upvotes'] and post_id not in users[user][u'upvotes']:
        if user in posts[post_id][u'downvotes'] and post_id in users[user][u'downvotes']:
            posts[post_id][u'downvotes'].remove(user)
            users[user][u'downvotes'].remove(post_id)
        else:
            posts[post_id][u'upvotes'].append(user)
            users[user][u'upvotes'].append(post_id)
    with open("posts.txt", 'w') as posts_file:
        json.dump(posts, posts_file)
    with open("users.txt", 'w') as users_file:
        json.dump(users, users_file)

def downvote(posts, users, user, post_id):
    post_id = post_id[8:]
    if user not in posts[post_id][u'downvotes'] and post_id not in users[user][u'downvotes']:
        if user in posts[post_id][u'upvotes'] and post_id in users[user][u'upvotes']:
            posts[post_id][u'upvotes'].remove(user)
            users[user][u'upvotes'].remove(post_id)
        else:
            posts[post_id]['downvotes'].append(user)
            users[user][u'downvotes'].append(post_id)
    with open("posts.txt", 'w') as posts_file:
        json.dump(posts, posts_file)
    with open("users.txt", 'w') as users_file:
        json.dump(users, users_file)

def inject_test_posts(posts):
    return {'23B393D1150ACB4': {'sentence': ['A', 'short', 'sentence'], 'upvotes': [], 'downvotes': []}, '3030DBB2BE1D411': {'sentence': ['Another', 'sentence'], 'upvotes': [], 'downvotes': []}}

def inject_test_sentences():
    return {u'226B79DB11270BA': {u'sentence': [u'Can', u'you', u'complete'], u'upvotes': [], u'downvotes': []}}

if __name__ == '__main__':
    import doctest
    doctest.testmod()
