from collections import defaultdict

data = open("test.txt")
data = open("data.txt")

connections = dict()
costmap = defaultdict(lambda: 0)

start = ""
row = 0
for line in data:
    line = line.strip("\n")
    pipes = list(line)
    print(pipes)
    col = 0
    for pipe in pipes:
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

max_cost = 0
queue = [(start, 0)]
while queue:
    node, cost = queue.pop(0)
    costmap[node] = cost
    max_cost = max(max_cost, cost)
    neighbours = connections[node]
    [queue.append((neighbour, cost+1)) for neighbour in neighbours if not costmap[neighbour]]

print(max_cost)
