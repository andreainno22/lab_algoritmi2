import random
from random import randint


def h(value, function, m):
    if function == "d":
        return value % m
    elif function == "m":
        A = random.random()
        return int(m * ((value * A) % 1))
