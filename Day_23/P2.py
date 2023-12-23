from copy import copy
from heapq import heappush, heappop
from collections import defaultdict
import time
data = open("test.txt")
data = open("data.txt")

forest = []
for line in data:
    forest.append(list(line.strip("\n")))


neighs = {".":[(1,0),(-1,0),(0,1),(0,-1)], ">":[(0,1)], "<":[(0,-1)], "v":[(1,0)], "^":[(1,0)]}

junctions = []
for r in range(1, len(forest)-1):
    for c in range(1, len(forest[0])-1):
        if forest[r][c] == ".":
            counter = 0
            for n in neighs["."]:
                dr, dc = n
                if forest[r+dr][c+dc] in set([".", "<", ">", "v", "^"]):
                    
                    counter += 1
            if counter > 2:
                junctions.append((r,c))

start = (0,1)
stop = (len(forest)-1, len(forest[0])-2)
junc_length = defaultdict(lambda: dict())
for junc in junctions:
    q = [(junc, (-1, -1), 0, set([junc]))]
    #q = [(0, (1,1), (0,1), 1, set([(0,1)]))]
    while q:
        curr, last, steps, visited = q.pop(0)
        row,col = curr
        if curr in [start, stop] or curr in junctions and curr != junc:
            junc_length[junc][curr] = steps
        else:
            new_visited = copy(visited)
            new_visited.add(curr)
            for n in neighs["."]:
                dr, dc = n
                nr = row + dr
                nc = col + dc
                new_node = (nr,nc)
                if forest[nr][nc] != "#" and new_node not in new_visited:
                    q.append((new_node, curr, steps+1, new_visited))

start_junc = ()
start_len = 0
stop_junc = ()
stop_len = 0
for junc in junctions:
    if start in junc_length[junc]:
        start_junc = junc
        start_len = junc_length[junc][start]
        print("Found start")
    if stop in junc_length[junc]:
        stop_junc = junc
        stop_len = junc_length[junc][stop]
        print("Found stop")

print(len(junc_length))
from functools import cache
@cache
def traverse(curr, steps, visited):
    if curr == stop_junc:
        #print("stop", steps)
        return steps
    new_visited = copy(set(visited))
    new_visited.add(curr)
    new_visited = tuple(new_visited)
    big_res = [-1]
    for n in junc_length[curr]:
        if n not in new_visited and n not in [start, stop]:
            res = traverse(n, steps + junc_length[curr][n], new_visited)
            big_res.append(res)
    return max(big_res)


res = traverse(start_junc, 0, tuple(set())) 
res = res + start_len + stop_len

print(res)