#!/usr/bin/env python

import json

def load_json(json_file):
    '''
    '''
    with open(json_file) as the_file:
        return json.load(the_file)

def words_set(wordlist):
    '''
    '''
    with open(wordlist) as words_file:
        return set(word.strip().lower() for word in words_file if word.strip())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
