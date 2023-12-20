

class Flipflop():
    name = ""
    output = []
    state = False
    def __init__(self, name, dests):
        self.name = name
        self.output = []
        for d in dests.split(", "):
            self.output.append(d)

    def signal(self, name, value):
        if value == "high":
            return []
        else:
            actions = []
            if not self.state:
                for o in self.output:
                    actions.append((self.name, o, "high"))
            else:
                for o in self.output:
                    actions.append((self.name, o, "low"))

            self.state = not self.state
            return actions


class Broadcaster():
    name = ""
    output = []
    def __init__(self, name, dests):
        self.name = name
        for d in dests.split(", "):
            self.output.append(d)

    def signal(self, name, value):
        actions = []
        for o in self.output:
            actions.append((self.name, o, value))
        return actions


class Conjunction():
    name = ""
    states = dict()
    output = []
    def __init__(self, name, dests):
        self.output = []
        self.states = dict()
        self.name = name
        for d in dests.split(", "):
            self.output.append(d)

    def add_input(self, name):
        self.states[name] = "low"

    def signal(self, name, value):
        self.states[name] = value
        out_value = "high"
        if set(self.states.values()) == set(["high"]):
            out_value = "low"
        actions = []
        for o in self.output:
            actions.append((self.name, o, out_value))
        return actions

class EmptySignal():
    name = ""
    output = []
    def __init__(self, name, dests):
        self.output = []
        self.name = name

    def signal(self, name, value):
        return []

file_name = "test.txt"
file_name = "data.txt"
data = open(file_name)

conjunctions = set()
modules = dict()
for line in data:
    line = line.strip("\n")
    src, dests = line.split("->")
    dests = dests[1:]
    module_type = src[0]
    name = src[1:-1]
    if src == "broadcaster ":
        b = Broadcaster(src[:-1], dests)
        modules[src[:-1]] = b
    elif module_type == "%":
        f = Flipflop(name, dests)
        modules[name] = f
    elif module_type == "&":
        c = Conjunction(name, dests)
        modules[name] = c 
        conjunctions.add(name)

data = open(file_name)
for line in data:
    line = line.strip("\n")
    src, dests = line.split("->")
    dests = dests[1:]
    name = src[1:-1]
    dests[1:]
    for d in dests.split(", "):
        if d in conjunctions:
            modules[d].add_input(name)

from tqdm import tqdm
low_count = 0
high_count = 0
for i in range(1000):
    q = [("button", "broadcaster", "low")]
    while q:
        curr = q.pop(0)
        
        src, dest, val = curr
        #print(src, val, dest)
        if val == "low":
            low_count += 1
        elif val == "high":
            high_count += 1
        else:
            assert False
        if i == 0 and dest not in modules.keys():
            modules[dest] = EmptySignal(dest, "")
        new_signals = modules[dest].signal(src,val)
        for s in new_signals:
            q.append(s)

print(low_count)
print(high_count)
print(low_count*high_count)
