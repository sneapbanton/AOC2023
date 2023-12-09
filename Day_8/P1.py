
data = open("test.txt")
data = open("data.txt")

path = dict()
instructions = []
for line in data:
    line = line.strip("\n")

    if line and "=" in line:
        key, values = line.split("=")
        key = key[:-1]
        left, right = map(str, values[2:-1].split(","))
        right = right[1:]
        path[key] = (left, right)

    elif line:
        instructions = list(line)

current_node = "AAA"
steps = 0
instr = 0
while current_node != "ZZZ":
    curr_instr = instructions[instr]
    if curr_instr == "L":
        current_node = path[current_node][0]
    elif curr_instr == "R":
        current_node = path[current_node][1]
    else:
        assert False
    steps += 1
    instr += 1
    if instr >= len(instructions):
        instr = 0

print(steps) 