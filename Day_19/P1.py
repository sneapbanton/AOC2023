
data = open("test.txt")
data = open("data.txt")


workflows = dict()
accepted = []

def workflow_decision(name, vals):
    rules = workflows[name]
    for rule in rules[:-1]:
        var, sign, val, dest = rule
        if sign == "<" and vals[var]<int(val):
            return dest
        elif sign == ">" and vals[var]>int(val):
            return dest
    return rules[-1]

big_res = 0
parts = False
for line in data:
    line = line.strip("\n")
    if not line:
        parts = True
    if not parts:
        workflow = []
        name, rule = line.split("{")
        subrules = (rule[:-1]).split(",")
        for rule in subrules:
            if ":" in rule:
                var = rule[0]
                sign = rule[1]
                val, dest = rule[2:].split(":")
                workflow.append([var, sign, val, dest])
            else:
                dest = rule
                workflow.append(dest)
        workflows[name] = workflow
        
    elif line:
        vals = dict()
        values = line[1:-1].split(",")
        for value in values:
            key, val = value.split("=")
            vals[key] = int(val)
        
        curr = "in"
        while curr not in ['A','R']:
            curr = workflow_decision(curr, vals)
        if curr == 'A':
            for val in vals.values():
                big_res += val
print(big_res)
