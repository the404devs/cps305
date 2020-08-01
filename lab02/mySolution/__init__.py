# CPS305 Lab 2
# 09/17/19 - Owen Goodwin
# It's late. I'm tired. Here's some crappy python.
# There's really not much to document, so I hope you'll understand.

import timeit
import matplotlib.pyplot as plt

def timingTest2():
    s="""\
d = {
    "a": "a",
    "b": "a",
    "c": "a",
    "d": "a",
    "e": "a",
    "f": "a",
    "g": "a",
    "h": "a",
    "i": "a",
    "j": "a",
    "k": "a",
    "l": "a",
    "m": "a",
    "n": "a",
    "o": "a",
    "p": "a",
    "q": "a",
    "r": "a",
    "s": "a",
    "t": "a",
    "u": "a",
    "v": "a",
    "w": "a",
    "x": "a",
    "y": "a",
    "z": "a"
}
l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    """
    for x in range(0, 10):
        plt.plot(timeit.timeit("del d['a']", setup=s, number=1), x, "ro")
        plt.plot(timeit.timeit("del d['m']", setup=s, number=1), x, "rs")
        plt.plot(timeit.timeit("del d['z']", setup=s, number=1), x, "r^")
        plt.plot(timeit.timeit("del l[0]", setup=s, number=1), x, "bo")
        plt.plot(timeit.timeit("del l[13]", setup=s, number=1), x, "bs")
        plt.plot(timeit.timeit("del l[25]", setup=s, number=1), x, "b^")

    plt.xlabel("Execution Time (s)")#Labels for the x- and y-axis
    plt.ylabel("Iteration")
#     timeit.timeit(print("hi"), number=1)

def timingTest1():
    s="""\
d = {
    "a": "a",
    "b": "a",
    "c": "a",
    "d": "a",
    "e": "a",
    "f": "a",
    "g": "a",
    "h": "a",
    "i": "a",
    "j": "a",
    "k": "a",
    "l": "a",
    "m": "a",
    "n": "a",
    "o": "a",
    "p": "a",
    "q": "a",
    "r": "a",
    "s": "a",
    "t": "a",
    "u": "a",
    "v": "a",
    "w": "a",
    "x": "a",
    "y": "a",
    "z": "a"
}
    """
    for x in range(0, 10):
        plt.plot(timeit.timeit("d.get('a')", setup=s, number=1), x, "ro")
        plt.plot(timeit.timeit("d.get('m')", setup=s, number=1), x, "go")
        plt.plot(timeit.timeit("d.get('z')", setup=s, number=1), x, "bo")
        plt.plot(timeit.timeit("d.update(a='mario')", setup=s, number=1), x, "rs")
        plt.plot(timeit.timeit("d.update(m='mario')", setup=s, number=1), x, "gs")
        plt.plot(timeit.timeit("d.update(z='mario')", setup=s, number=1), x, "bs")

    plt.xlabel("Execution Time (s)")#Labels for the x- and y-axis
    plt.ylabel("Iteration")
 
timingTest2()