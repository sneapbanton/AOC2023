import numpy as np
from copy import copy
from tqdm import tqdm
from functools import cache
from collections import defaultdict

data = open("test.txt")
data = open("data.txt")

@cache
def move_rocks_north(rocks: np.array):
    rocks = np.array(rocks)
    c_rocks = copy(rocks)
    for c in range(rocks.shape[1]):
        col = ("".join(rocks[:,c].tolist())).split("#")
        a = np.where(rocks[:,c]=="#")[0].tolist()

        new_col = ""
        if 0 in a:
            new_col += "#"
            col = col[1:]

        for obj in col:
            length = len(obj)
            nrocks = obj.count("O")
            new_col += nrocks*"O" + "."*(length-nrocks) + "#"
        if len(new_col) != len(col):
            new_col = new_col[:-1]
        c_rocks[:,c] = np.array(list(new_col))
    return tuple(c_rocks)

def move_rocks_west(rocks: np.array):
    t_rocks = np.transpose(rocks)
    return np.transpose(np.array(move_rocks_north(to_tuple(t_rocks))))

def move_rocks_south(rocks: np.array):
    t_rocks = np.flipud(rocks)
    return np.flipud(np.array(move_rocks_north(to_tuple(t_rocks))))

def move_rocks_east(rocks: np.array):
    t_rocks = np.transpose(np.fliplr(rocks))
    return np.fliplr(np.transpose(np.array(move_rocks_north(to_tuple(t_rocks)))))

def to_tuple(rocks):
    rocks_list = rocks.tolist()
    new_rocks = tuple([tuple(x) for x in rocks_list])
    return new_rocks

def print_rocks(rocks):
    for r in range(rocks.shape[0]):
        rock_row = ""
        for c in range(rocks.shape[1]):
            rock_row += rocks[r,c]
        print(rock_row)

def extract_result(rocks):
    result = 0
    for row in range(rocks.shape[0]):
        for col in range(rocks.shape[1]):
            if rocks[row, col] == "O":
                result += rocks.shape[0] - (row)
    return (result)

rocks = []
for line in data:
    rocks.append(list(line.strip("\n")))

res = []
east_rocks = np.array(rocks)
i = 0
jumped = False
while i < 1_000_000_000:
    north_rocks = np.array(move_rocks_north(to_tuple(east_rocks)))
    west_rocks = move_rocks_west(north_rocks)
    south_rocks = move_rocks_south(west_rocks)
    east_rocks = move_rocks_east(south_rocks)

    result = extract_result(east_rocks)
    if result in res and not jumped:
        print([x for x in res if x <91016 and x > 90946])
        cycle_len = len(res)
        jumped = True
        i = (cycle_len * int(1_000_000_000 / cycle_len)) + 1
        print(i)
    if i > 3000 and not jumped:
        res.append(result)
    
    i += 1

print(extract_result(east_rocks))


# 91016 too high