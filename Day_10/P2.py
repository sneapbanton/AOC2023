from collections import defaultdict

data = open("test.txt")
#data = open("data.txt")

connections = defaultdict(lambda: [])
symbols = dict()
costmap = defaultdict(lambda: 0)

start = ""
row = 0
for line in data:
    line = line.strip("\n")
    pipes = list(line)
    print(pipes)
    col = 0
    for pipe in pipes:
        symbols[(row, col)] = pipe
        if pipe == "7":
            connections[(row, col)] = [(row, col-1), (row+1,col)]
        elif pipe == "J":
            connections[(row, col)] = [(row, col-1), (row-1,col)]
        elif pipe == "L":
            connections[(row, col)] = [(row, col+1), (row-1,col)]
        elif pipe == "F":
            connections[(row, col)] = [(row, col+1), (row+1,col)]
        elif pipe == "-":
            connections[(row, col)] = [(row, col-1), (row,col+1)]
        elif pipe == "|":
            connections[(row, col)] = [(row+1, col), (row-1,col)]
        elif pipe == "S":
            start = (row,col)
        col += 1
    row += 1

start_neighbours = [neigh for neigh in connections.keys() if start in connections[neigh]]
connections[start] = start_neighbours


queue = [(start, 0)]
loop = set()
while queue:
    node, cost = queue.pop(0)
    loop.add(node)
    costmap[node] = cost
    neighbours = connections[node]
    [queue.append((neighbour, cost+1)) for neighbour in neighbours if not costmap[neighbour]]

queue = []

for r in range(row):
    queue.append((r, 0))
    queue.append((r, col))

non_inner = 0
visited = set()
while queue:
    node = queue.pop(0)
    if node not in loop and node not in visited:
        visited.add(node)
        non_inner += 1
        neighbours = [(node[0]-1,node[1]), (node[0]+1,node[1]), (node[0],node[1]-1), (node[0],node[1]+1)]

        if (node[0]-1, node[1]) in loop and symbols[(node[0]-1, node[1])]:
            neighbours.append((node[0]-1, node[1]))
        [queue.append(neighbour) for neighbour in neighbours if 0<=neighbour[0]<row and 0<neighbour[1]<col and symbols[neighbour] in ["7", "F", "J", "L"]]
    elif node in loop and node not in visited:
        visited.add(node)
        [queue.append(neighbour) for neighbour in connections[node] if neighbour not in visited]



inner = 0
for r in range(row):
    row = ""
    for c in range(col):
        if (r,c) in visited and (r,c) not in loop:
            row += "o"
        elif (r,c) in loop:
            row += "-"
        else:
            row += "+"
            inner += 1
    print(row)

print(inner)