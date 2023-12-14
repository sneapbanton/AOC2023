import numpy as np
from copy import copy
from tqdm import tqdm

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

def find_horizontal(rocks: np.array, old_val):
    match = -1
    for r in range(rocks.shape[0]-1):
        if(rocks[r,:].tolist() == rocks[r+1,:].tolist()):
            if match_horizontal(rocks, r) and r != old_val:
                match = r
                break

    return match+1 if match != -1 else 0

def find_vertical(rocks: np.array, old_val):
    match = -1
    for c in range(rocks.shape[1]-1):
        if(rocks[:,c].tolist() == rocks[:,c+1].tolist()):
            if match_vertical(rocks, c) and c != old_val:
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
for ro in tqdm(range(len(patterns))):
    rock = patterns[ro]
    horizontal_index = find_horizontal(rock, -1)
    vertical_index = find_vertical(rock, -1)
    for row in range(rock.shape[0]):
        for col in range(rock.shape[1]):
            c_rocks = copy(rock)
            c_rocks[row, col] = "#" if c_rocks[row, col] == "." else "."
            new_horizontal_index = find_horizontal(c_rocks, horizontal_index-1)
            new_vertical_index = find_vertical(c_rocks, vertical_index-1)
            if (new_horizontal_index or new_vertical_index) and (horizontal_index != new_horizontal_index or not horizontal_index) and (vertical_index != new_vertical_index or not vertical_index):
                break
        if (new_horizontal_index or new_vertical_index) and (horizontal_index != new_horizontal_index or not horizontal_index) and (vertical_index != new_vertical_index or not vertical_index):
                break
            
    result += new_horizontal_index * 100
    result += new_vertical_index

print(result)