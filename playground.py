import functools
import random

points = [[3,20,2],[100,9,4],[4,10,10]]
top = functools.reduce(lambda x, y: x if x[1] > y[1] else y,points)
bot = functools.reduce(lambda x, y: x if x[1] < y[1] else y,points)
points.remove(top)
points.remove(bot)
mid = points[0]

print(top,mid,bot)