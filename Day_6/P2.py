
data = open("test.txt")
data = open("data.txt")

factor = 1

times = []
dists = []

rows = []

for line in data:
    line = line.strip("\n")
    rows.append(line)

times = [x for x in rows[0].split(" ") if "Time:" in rows[0] and x != "" and x.isnumeric()]
dists = [x for x in rows[1].split(" ") if "Distance:" in rows[1] and x != "" and x.isnumeric()]

time = ""
dist = ""
for i in range(len(times)):
    time += times[i]
    dist += dists[i]

time = int(time)
dist = int(dist)

ways = 0
for w in range(time):
    total_dist = w * (time - w)
    if (total_dist > dist):
        ways += 1
factor = factor * ways

print(factor)