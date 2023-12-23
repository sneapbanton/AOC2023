from copy import copy

data = open("test.txt")
data = open("data.txt")

forest = []
for line in data:
    forest.append(list(line.strip("\n")))

neighs = {".":[(1,0),(-1,0),(0,1),(0,-1)], ">":[(0,1)], "<":[(0,-1)], "v":[(1,0)], "^":[(1,0)]}
q = [((1,1), (0,1), 1, set([(0,1)]))]
res = []
while q:
    curr, last, steps, visited = q.pop(0)
    row,col = curr
    if row == len(forest)-1:
        res.append(steps)
    else:
        new_visited = copy(visited)
        new_visited.add(curr)
        for n in neighs[forest[row][col]]:
            dr, dc = n
            nr = row + dr
            nc = col + dc
            new_node = (nr,nc)
            if forest[nr][nc] != "#" and new_node not in new_visited:
                q.append((new_node, curr, steps+1, new_visited))

print(res)
print(max(res))