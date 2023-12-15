import numpy as np
from copy import copy
data = open("test.txt")
data = open("data.txt")


def move_rocks_north(rocks: np.array):
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
    return c_rocks

rocks = []
for line in data:
    rocks.append(list(line.strip("\n")))

rocks = np.array(rocks)
front_rocks = move_rocks_north(rocks)
result = 0
for row in range(rocks.shape[0]):
    for col in range(rocks.shape[1]):
        if front_rocks[row, col] == "O":
            result += rocks.shape[0] - (row)
print(result)