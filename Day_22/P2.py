


class sandblock():
    def __init__(self, name, start, end):
        self.name = str(name)
        self.points = []
        for i in range(3):
            vals = list(range(start[i],end[i]+1))
            self.points.append(vals)
        tmp = []
        for x in self.points[0]:
            for y in self.points[1]:
                for z in self.points[2]:
                    tmp.append((x,y,z))
        self.points = tmp

data = open("test.txt")
data = open("data.txt")

name = 0
blocks = []
for line in data:
    start, end = line.strip("\n").split("~")
    x, y, z = map(int, start.split(","))
    start = (x,y,z)
    x, y, z = map(int, end.split(","))
    end = (x,y,z)
    sb = sandblock(name,start,end)
    blocks.append(sb)
    name += 1


from collections import defaultdict
box = defaultdict(lambda: ".")
for block in blocks:
    name = block.name
    for p in block.points:
        box[p] = name

Falling = True
while Falling:
    Falling = False
    for block in blocks:
        name = block.name
        fall = True
        for p in block.points:
            new_p = (p[0], p[1], p[2]-1)
            if p[2]-1 < 0 or box[new_p] not in set([".", name]):
                fall = False
        if fall:
            Falling = True
            nps = []
            for p in block.points:
                box[p] = "."
                new_p = (p[0], p[1], p[2]-1)
                box[new_p] = name
                nps.append(new_p)
            block.points = nps
    
maxs = [0,0,0]
for block in blocks:
    for p in block.points:
        x,y,z = p
        maxs[0] = max(x,maxs[0])
        maxs[1] = max(y,maxs[1])
        maxs[2] = max(z,maxs[2])

supports = defaultdict(lambda: set())
for z in range(maxs[2]):
    for y in range(maxs[1]+1):
        for x in range(maxs[0]+1):
            if box[(x,y,z)] != box[(x,y,z+1)] and box[(x,y,z+1)] != ".":
                supports[box[(x,y,z)]].add(box[(x,y,z+1)])

import copy
from tqdm import tqdm
res = 0
for target in tqdm(blocks):
    target_name = target.name
    cbox = copy.deepcopy(box)
    for p in target.points:
        cbox[p] = "."

    cblocks = [copy.deepcopy(x) for x in blocks]
    Falling = True
    fallen = set()
    while Falling:
        Falling = False
        for block in cblocks:
            if block == target:
                continue
            name = block.name
            fall = True
            for p in block.points:
                new_p = (p[0], p[1], p[2]-1)
                if p[2]-1 < 0 or cbox[new_p] not in set([".", name]):
                    fall = False
            if fall:
                Falling = True
                fallen.add(name)
                nps = []
                for p in block.points:
                    cbox[p] = "."
                    new_p = (p[0], p[1], p[2]-1)
                    cbox[new_p] = name
                    nps.append(new_p)
                block.points = nps
    #print(target_name, fallen)
    res += len(fallen)


print(res)