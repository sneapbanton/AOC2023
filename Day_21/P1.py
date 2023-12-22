from functools import cache
from collections import defaultdict

data = open("test.txt")
data = open("data.txt")

garden = []

even = defaultdict(lambda: -1)
odd = defaultdict(lambda: -1)
visited = set()
def traverse(row, col, steps):
    #print(row, col, steps)
    if steps == 0:
        visited.add((row,col))
        return
    
    if steps % 2 == 0:
        even[(row, col)] = steps
        visited.add((row,col))
    else:
        odd[(row, col)] = steps
        

    neighs = [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]
    for neigh in neighs:
        r, c = neigh
        if 0<=r<len(garden) and 0<=c<len(garden[0]) and garden[r][c] != "#":
            if (steps-1) % 2 == 0 and steps-1 > even[(r,c)] or (steps-1) % 2 == 1 and steps-1 > odd[(r,c)]:
                traverse(r, c, steps-1)
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

traverse(start[0], start[1], 64)
print(len(visited))
