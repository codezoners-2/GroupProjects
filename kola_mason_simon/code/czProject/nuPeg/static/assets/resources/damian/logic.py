from __future__ import division

import random
import math


def makeStack(n):
    return [{'rgb': [0, 0, 0],
             'x': i / n,
             'y': i / n,
             'r': 0.1,
             'key': i} for i in range(n)]


def makeDots(n):
    randR = random.randint(0, 255)
    randG = random.randint(0, 255)
    randB = random.randint(0, 255)
    return [{'rgb': [randR, randG, randB],
             'x': random.random(),
             'y': random.random(),
             'r': random.random(),
             'key': i} for i in range(n)]
