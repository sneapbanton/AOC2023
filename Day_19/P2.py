
data = open("test.txt")
data = open("data.txt")

workflows = dict()

def invert_sign(s):
    if s == "<":
        return ">="
    else:
        return "<="

def recurser(name):
    result = []
    rules = workflows[name]
    passed_rules = []
    for rule in rules[:-1]:
        var, sign, val, dest = rule
        if dest == "R":
            pass
        elif dest == "A":
            new_result = []
            new_result.append([var,sign,val])
            [new_result.append(x) for x in passed_rules]
            result.append(new_result)
        else:
            future_rules = recurser(dest)
            for combs in future_rules:
                [combs.append(x) for x in passed_rules]
                combs.append([var,sign,val])
                result.append(combs)
        passed_rules.append([var,invert_sign(sign),val])
    if rules[-1] == "A":
        result.append(passed_rules)
    elif rules[-1] != "R":
        sub_results = recurser(rules[-1])
        for s in sub_results:
            [s.append(x) for x in passed_rules]
            result.append(s)
    return result
            

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

ranges = recurser("in")

from collections import defaultdict

combs = 0
for rules in ranges:
    maxes = defaultdict(lambda: 4000)
    minis = defaultdict(lambda: 0)
    for rule in rules:
        var, sign, val = rule
        if sign == "<=":
            maxes[var] = min(maxes[var], int(val))
        elif sign == "<":
            maxes[var] = min(maxes[var], int(val)-1)
        if sign == ">=":
            minis[var] = max(minis[var], int(val)-1)
        elif sign == ">":
            minis[var] = max(minis[var], int(val))
    x = maxes["x"] - minis["x"]
    m = maxes["m"] - minis["m"]
    a = maxes["a"] - minis["a"]
    s = maxes["s"] - minis["s"]
    combs += abs(x*m*a*s)
print(combs)