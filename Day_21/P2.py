import math
from collections import defaultdict

data = open("test.txt")
data = open("data.txt")

garden = []

nodes = defaultdict(lambda: math.inf)
total_step = 0
def traverse(row, col, steps):
    if steps == total_step:
        return
        
    neighs = [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]
    for neigh in neighs:
        r, c = neigh
        rm = r%len(garden)
        cm = c%len(garden[0])
        if garden[rm][cm] != "#" and steps+1 < nodes[neigh]:
            nodes[neigh] = steps + 1
            traverse(r, c, steps+1)
    return



start = 0
found = False
for line in data:
    line = line.strip("\n")
    garden.append(list(line))
    if "S" in list(line):
        start = (start, list(line).index("S"))
        found = True
    elif not found:
        start += 1

import numpy as np
r = []
half = start[0]
side = len(garden)
for i in [half, half+side, (half+2*side)]:
    nodes[(start[0], start[1])] = 0
    total_step = i
    traverse(start[0], start[1], 0)
    res = len([x for x in nodes if nodes[x]%2 == total_step%2])
    r.append(res)
    nodes = defaultdict(lambda: math.inf)

N = 202300
c = r[0]
a = (r[2] - 2*r[1] + r[0]) / 2
b = r[1] - r[0] - a
f = lambda n: a*n**2 + b*n + c
print(int(f(N)))
