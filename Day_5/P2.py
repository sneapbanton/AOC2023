from collections import defaultdict


def key_mapper(rules, end, start, n):
    rules.append((end,start,n))

data = open("test.txt")
data = open("data.txt")

lines = []
for line in data:
    line = line.strip("\n")
    lines.append(line)

lines.append("")

seeds = []
sts = []
stf = []
ftw = []
wtl = []
ltt = []
tth = []
htl = []

i = 0
while i < len(lines):
    j = 1
    if ("seeds" in lines[i]):
        se = lines[i].split(" ")[1:]
        for si in range(0, int(len(se)), 2):
            seeds.append((se[si], se[si+1]))
        i += 1

    elif ("seed-to-soil" in lines[i]):
        while (lines[i+j] != ""):
            s_start, s_end, n = map(int, lines[i+j].split(" "))
            key_mapper(sts, s_start, s_end, n)
            j += 1
        i += j

    elif ("soil-to-fertilizer" in lines[i]):
        while (lines[i+j] != ""):
            s_start, s_end, n = map(int, lines[i+j].split(" "))
            key_mapper(stf, s_start, s_end, n)
            j += 1
        i += j

    elif ("fertilizer-to-water" in lines[i]):
        while (lines[i+j] != ""):
            s_start, s_end, n = map(int, lines[i+j].split(" "))
            key_mapper(ftw, s_start, s_end, n)
            j += 1
        i += j

    elif ("water-to-light" in lines[i]):
        while (lines[i+j] != ""):
            s_start, s_end, n = map(int, lines[i+j].split(" "))
            key_mapper(wtl, s_start, s_end, n)
            j += 1
        i += j

    elif ("light-to-temperature" in lines[i]):
        while (lines[i+j] != ""):
            s_start, s_end, n = map(int, lines[i+j].split(" "))
            key_mapper(ltt, s_start, s_end, n)
            j += 1
        i += j

    elif ("temperature-to-humidity" in lines[i]):
        while (lines[i+j] != ""):
            s_start, s_end, n = map(int, lines[i+j].split(" "))
            key_mapper(tth, s_start, s_end, n)
            j += 1
        i += j

    elif ("humidity-to-location" in lines[i]):
        while (lines[i+j] != "" and i+j < len(lines)):
            s_start, s_end, n = map(int, lines[i+j].split(" "))
            key_mapper(htl, s_start, s_end, n)
            j += 1
        i += j

    else:
        i += 1


def get_value(d, k):
    for rule in d:
        if k in range(rule[0], rule[0] + rule[2]):
            return rule[1] + (k-rule[0])
    return k


location = 0
lowest_location = -1
while lowest_location == -1:
    humi = get_value(htl, location)
    temp = get_value(tth, humi)
    ligh = get_value(ltt, temp)
    wate = get_value(wtl, ligh)
    fert = get_value(ftw, wate)
    soil = get_value(stf, fert)
    seed = get_value(sts, soil)

    for rule in seeds:
        if int(rule[0]) <= seed and seed < int(rule[0]) + int(rule[1]):
            lowest_location = location
    location += 1
    if (location % 10000 == 0):
        print(location)

# Backwards solver compared to part 1, took 1 hour of runtime to find the answer

print(lowest_location)