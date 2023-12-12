import numpy as np
import tqdm

data = open("test.txt")
data = open("data.txt")

space = []

for line in data:
    line = line.strip("\n")
    line = list(line)
    space.append(line)

space = np.array(space)
rows, cols = space.shape

r = 0
while r < rows:
    if len(set(space[r,:])) == 1:
        space = np.insert(space, r, ".", axis=0)
        rows += 1
        r += 2
    else:
        r += 1

c = 0
while c < cols:
    if len(set(space[:,c])) == 1:
        space = np.insert(space, c, ".", axis=1)
        c += 1
        cols += 1
    c += 1


nodes = []
for r in range(rows):
    for c in range(cols):
        if space[r,c] == "#":
            nodes.append((r,c))

from collections import defaultdict
import math, heapq
def dijsktra(start):
    q = []
    costs = defaultdict(lambda: math.inf)
    prev = defaultdict(lambda: -1)
    costs[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, node = heapq.heappop(q)
        
        r, c = node
        if (0<=r<rows and 0<=c<cols):
            neighs = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            neighs = [neigh for neigh in neighs if costs[neigh] > cost+1]
            for neigh in neighs:
                costs[neigh] = cost+1
                prev[neigh] = node
                heapq.heappush(q, (cost+1, neigh))
    
    return costs

all_costs = []
for i in tqdm.tqdm(range(len(nodes))):
    node = nodes[i]
    costs = dijsktra(node)
    all_costs.append(costs)

result = 0
for i in range(len(nodes)):
    for j in range(i, len(nodes)):
        if i != j:
            result += all_costs[i][nodes[j]]
print(result)
