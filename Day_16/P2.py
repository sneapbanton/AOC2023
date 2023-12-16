from functools import cache

data = open("test.txt")
data = open("data.txt")

karta = []
for line in data:
    line = line.strip("\n")
    karta.append(list(line))

def new_pos(row, col, vectors):
    nodes = []
    for vector in vectors:
        new_row = row + vector[0]
        new_col = col + vector[1]
        if 0<=new_row<len(karta) and 0<=new_col<len(karta[0]):
            nodes.append((new_row, new_col, vector))
    return nodes

@cache
def calculate_next(row, col, dir):
    symbol = karta[row][col]
    vectors = []
    if symbol == ".":
        vectors.append(dir)

    elif symbol == "/":
        if dir == (0,1):
            vectors.append((-1,0))
        elif dir == (0,-1):
            vectors.append((1,0))
        if dir == (1,0):
            vectors.append((0,-1))
        elif dir == (-1,0):
            vectors.append((0,1))

    elif symbol == "\\":
        if dir == (0,1):
            vectors.append((1,0))
        elif dir == (0,-1):
            vectors.append((-1,0))
        if dir == (1,0):
            vectors.append((0,1))
        elif dir == (-1,0):
            vectors.append((0,-1))

    elif symbol == "-":
        if dir == (1,0) or dir == (-1,0):
            vectors.append((0,1))
            vectors.append((0,-1))
        else:
            vectors.append(dir)

    elif symbol == "|":
        if dir == (0,1) or dir == (0,-1):
            vectors.append((1,0))
            vectors.append((-1,0))
        else:
            vectors.append(dir)

    new_nodes = new_pos(row, col, vectors)
    return new_nodes

def generate_lava(start):
    visited = set()
    visited_pos = set()
    old_len = -1
    q = [start]
    new_q = []
    while old_len != len(visited):
        old_len = len(visited)
        while q:
            curr = q.pop(0)
            visited_pos.add((curr[0],curr[1]))
            new_nodes = calculate_next(*curr)
            visited.add(curr)
            for node in new_nodes:
                if node not in visited:
                    new_q.append(node)
        q = new_q

    res = 0
    for r in range(len(karta)):
        print_r = ""
        for c in range(len(karta[0])):
            if (r,c) in visited_pos:
                print_r += "#"
                res += 1
            else:
                print_r += "."
        #print(print_r)

    return res

start_nodes = []
[start_nodes.append((0,x,(1,0))) for x in range(len(karta[0]))]
[start_nodes.append((len(karta)-1,x,(-1,0))) for x in range(len(karta[0]))]
[start_nodes.append((x,0,(0,1))) for x in range(len(karta))]
[start_nodes.append((x,len(karta[0])-1,(0,-1))) for x in range(len(karta))]
best_res = 0
for start in start_nodes:
    res = generate_lava(start)
    best_res = res if res > best_res else best_res
print(best_res)