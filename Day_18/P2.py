import numpy as np

data = open("test.txt")
data = open("data.txt")

points = [(0,0)]
row = 0
col = 0
for line in data:
    d, n, color = line.strip("\n").split(" ")
    color = color[1:-1]
    n = int(color[1:-1],16)
    d = color[-1]
    n = int(n)
    old_row = row
    old_col = col
    if d == "3":
        row -= n
    elif d == "1":
        row += n
    elif d == "2":
        col -= n
    elif d == "0":
        col += n
    points.append((row, col))
points = np.transpose(np.array(points))
res = 0
border = 0
for pair in range(points.shape[1]-1):
    p = points[:,pair:pair+2]
    res += np.linalg.det(p)
    border += abs(p[0,0]-p[0,1]) + abs(p[1,0]-p[1,1])

print(abs(int(res/2)) + int(border/2) + 1)
