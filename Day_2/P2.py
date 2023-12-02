
data = open("test.txt")
data = open("data.txt")

sum_factor = 0
for line in data:
    line = line.strip("\n")
    info = line.split(":")
    id = int(info[0].split(" ")[1])

    sets = info[1].split(";")
    greens = []
    blues =  []
    reds = []
    for subset in sets:
        cubes = subset.split(",")
        for cube in cubes:
            value = int(cube.split(" ")[1])
            if "red" in cube:
                reds.append(value)
            elif "blue" in cube:
                blues.append(value)
            elif "green" in cube:
                greens.append(value)
    factor = max(reds)*max(greens)*max(blues)
    sum_factor += factor


print(sum_factor)

