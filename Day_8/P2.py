
import math

data = open("test.txt")
data = open("data.txt")

path = dict()
instructions = []
starting_nodes = []
for line in data:
    line = line.strip("\n")

    if line and "=" in line:
        key, values = line.split("=")
        key = key[:-1]
        left, right = map(str, values[2:-1].split(","))
        right = right[1:]
        path[key] = (left, right)
        if key[-1] == "A":
            starting_nodes.append(key)

    elif line:
        instructions = list(line)

print(len(starting_nodes))

def prime_def():
    return 0

s = []
for i in range(len(starting_nodes)):
    steps = 0
    instr = 0
    current_node = starting_nodes[i]
    old_len_set = -1
    while True:
        curr_instr = instructions[instr]
        if curr_instr == "L":
            current_node = path[current_node][0]
        elif curr_instr == "R":
            current_node = path[current_node][1]
        else:
            assert False

        steps += 1
        instr = (instr + 1) % len(instructions)
        if (current_node[-1] == "Z"):
            print(steps)
            s.append(steps)
            break
    print()


print(math.lcm(*s))