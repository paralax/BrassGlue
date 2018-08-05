#!/usr/bin/env python

import random
import sys

from flask import Flask, render_template

sys.stdout = sys.stderr

app = Flask(__name__)
app.debug = True

@app.route('/')
def root():
    # in the style of frog team names ... 

    one = ('adjectives', 'elements', 'metals', 'moods', 'verbs', 'sizes', 'gerunds', 'adverbs')
    two = ('animals', 'boats', 'dogs', 'flowers', 'reptiles', 'weapons', 'birds',
           'fish', 'cats', 'fruit', 'plants', 'tools', 'shapes', 'music', 'spices')
    
    with open('wordlists/' + random.choice(one), 'r') as f:
        first = [ x.strip() for x in f.readlines() ]
        first = filter(lambda x: len(x) > 1, first)
        
    with open('wordlists/' + random.choice(two), 'r') as f:
        second = [ x.strip() for x in f.readlines() ]
        second = filter(lambda x: len(x) > 1, second)

    names = []
    for i in range(20):
        names.append('%s %s' % (random.choice(first).split()[-1],
                                random.choice(second).split()[-1]))
    html = render_template('index.html', names=names)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
