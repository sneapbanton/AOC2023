
data = open("test.txt")
data = open("data.txt")

factor = 1

times = []
dists = []

rows = []

for line in data:
    line = line.strip("\n")
    rows.append(line)

times = [int(x) for x in rows[0].split(" ") if "Time:" in rows[0] and x != "" and x.isnumeric()]
dists = [int(x) for x in rows[1].split(" ") if "Distance:" in rows[1] and x != "" and x.isnumeric()]

for i in range(0, len(times)):
    ways = 0
    time = times[i]
    for w in range(time):
        total_dist = w * (time - w)
        if (total_dist > dists[i]):
            ways += 1
    if ways:
        factor = factor * ways

print(factor)