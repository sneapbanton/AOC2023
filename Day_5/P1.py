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
        for s in se:
            seeds.append(int(s))
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
        if k in range(rule[1], rule[1] + rule[2]):
            return rule[0] + (k-rule[1])
    return k

locations = []
for seed in seeds:
    print()
    soil = get_value(sts, seed)
    print(soil)
    fert = get_value(stf, soil)
    print(fert)
    wate = get_value(ftw, fert)
    print(wate)
    ligh = get_value(wtl, wate)
    print(ligh)
    temp = get_value(ltt, ligh)
    print(temp)
    humi = get_value(tth, temp)
    print(humi)
    loca = get_value(htl, humi)
    print(loca)
    locations.append(loca)

print()
print(min(locations))