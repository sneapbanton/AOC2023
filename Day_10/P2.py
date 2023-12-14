from collections import defaultdict

data = open("test.txt")
start_symbol = "7"
data = open("data.txt")
start_symbol = "-"

connections = defaultdict(lambda: [])
symbols = dict()
costmap = defaultdict(lambda: 0)

start = ""
row = 0
for line in data:
    line = line.strip("\n")
    pipes = list(line)
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

symbols[start] = start_symbol

inside = 0
for r in range(row):
    prow = ""
    pipes_passed = 0
    F_passed = 0
    L_passed = 0
    for c in range(col):
        if (r,c) in loop:
            symbol = symbols[(r,c)]
            prow += symbol
            if symbol in set(["|", "F", "7"]):
                pipes_passed += 1
        elif sum([pipes_passed,F_passed, L_passed]) % 2 == 1:
            inside += 1
            prow += "+"
        else:
            prow += "."
    print(prow)

print(inside)