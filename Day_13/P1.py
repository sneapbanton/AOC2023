import numpy as np


data = open("test.txt")
data = open("data.txt")

def match_horizontal(rocks, r):
    r1 = r
    r2 = r+1
    while r2 < rocks.shape[0] and r1 >= 0:
        if rocks[r1,:].tolist() != rocks[r2,:].tolist():
            return False
        r1 += -1
        r2 += 1

    return True

def match_vertical(rocks, c):
    c1 = c
    c2 = c+1
    while c2 < rocks.shape[1] and c1 >= 0:
        if rocks[:, c1].tolist() != rocks[:, c2].tolist():
            return False
        c1 += -1
        c2 += 1

    return True

def find_horizontal(rocks: np.array):
    match = -1
    for r in range(rocks.shape[0]-1):
        if(rocks[r,:].tolist() == rocks[r+1,:].tolist()):
            if match_horizontal(rocks, r):
                match = r
                break

    return match+1 if match != -1 else 0

def find_vertical(rocks: np.array):
    match = -1
    for c in range(rocks.shape[1]-1):
        if(rocks[:,c].tolist() == rocks[:,c+1].tolist()):
            if match_vertical(rocks, c):
                match = c
                break

    return match+1 if match != -1 else 0

patterns = []
rocks = []
for line in data:
    line = line.strip("\n")
    if line:
        rocks.append(list(line))
    else:
        patterns.append(np.array(rocks))
        rocks = []
patterns.append(np.array(rocks))

result = 0
for rock in patterns:
    horizontal_index = find_horizontal(rock)
    result += horizontal_index * 100
    vertical_index = find_vertical(rock)
    result += vertical_index

print(result)