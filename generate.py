#!/usr/bin/python

import random
import sys

# in the style of frog team names ... 

one = ('adjectives', 'elements', 'metals', 'verbs', 'gems',)
two = ('animals', 'boats', 'dogs', 'flowers', 'reptiles', 'weapons', 'birds', 
       'fish', 'cats', 'fruit', 'plants', 'tools',)

with open('wordlists/' + random.choice(one), 'r') as f:
    first = [ x.strip() for x in f.readlines() ]
    first = filter(lambda x: len(x) > 1, first)

with open('wordlists/' + random.choice(two), 'r') as f:
    second = [ x.strip() for x in f.readlines() ]
    second = filter(lambda x: len(x) > 1, second)

try: N = int(sys.argv[1])
except IndexError: N = 20
for i in range(N):
    print random.choice(first).split()[-1],
    print random.choice(second).split()[-1]
    
