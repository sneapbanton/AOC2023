
data = open("test.txt")
data = open("data.txt")

sum_ids = 0
for line in data:
    line = line.strip("\n")
    info = line.split(":")
    id = int(info[0].split(" ")[1])

    sets = info[1].split(";")
    possible = True
    for subset in sets:
        green = 0
        blue = 0
        red = 0
        cubes = subset.split(",")
        for cube in cubes:
            value = int(cube.split(" ")[1])
            if "red" in cube:
                red += value
            elif "blue" in cube:
                blue += value
            elif "green" in cube:
                green += value
        if red > 12 or green > 13 or blue > 14:
            possible = False
    if possible:
        print("id ", id)
        sum_ids += id


print(sum_ids)

