
data = open("test.txt")
data = open("data.txt")

points = set([(0,0)])
row = 0
col = 0
max_row = 0
max_col = 0
min_row = 0
min_col = 0
for line in data:
    d, n, color = line.strip("\n").split(" ")
    n = int(n)
    old_row = row
    old_col = col
    if d == "U":
        row -= n
    elif d == "D":
        row += n
    elif d == "L":
        col -= n
    elif d == "R":
        col += n
    [points.add((x, old_col)) for x in range(min(old_row, row), max(old_row, row))]
    [points.add((old_row, x)) for x in range(min(old_col, col), max(old_col, col))]
    points.add((row, col))
    max_row = max(max_row, row)
    max_col = max(max_col, col)
    min_row = min(min_row, row)
    min_col = min(min_col, col)

for r in range(min_row, max_row+1):
    row = ""
    for c in range(min_col, max_col+1):
        if (r,c) in points:
            row += "#"
        else:
            row += "."
    print(row)

q = []
min_nodes = [x for x in points if x[0] == min_row]
q.append((min_row+1, min_nodes[0][1]+1))
while q:
    curr = q.pop(0)
    row, col = curr
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
        new_row = row + d[0]
        new_col = col + d[1]
        new_node = (new_row,new_col)
        if new_node not in points:
            points.add(new_node)
            q.append(new_node)

# Flood-fill (node):
#   1. Set Q to the empty queue or stack.
#   2. Add node to the end of Q.
#   3. While Q is not empty:
#   4.   Set n equal to the first element of Q.
#   5.   Remove first element from Q.
#   6.   If n is Inside:
#          Set the n
#          Add the node to the west of n to the end of Q.
#          Add the node to the east of n to the end of Q.
#          Add the node to the north of n to the end of Q.
#          Add the node to the south of n to the end of Q.
#   7. Continue looping until Q is exhausted.
#   8. Return.

print()
    
for r in range(min_row, max_row+1):
    row = ""
    for c in range(min_col, max_col+1):
        if (r,c) in points:
            row += "#"
        else:
            row += "."
    print(row)

print(len(points))