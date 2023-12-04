from collections import defaultdict

def def_value():
    return []

data = open("test.txt")
data = open("data.txt")

machine = []

for line in data:
    line = str.strip(line, "\n")
    machine.append("." + line + ".")

empty_row = len(machine[0])*"."
machine.insert(0, empty_row)
machine.append(empty_row)

gear_pos = defaultdict(def_value)

summer = 0
for r in range(1,len(machine)-1):    
    number = ""
    for c in range(1,len(machine[r])):
        if str.isnumeric(machine[r][c]):
            number += machine[r][c]
        else:
            if number:
                colmin = c - 1 - len(number)
                colmax = c + 1
                array = []

                array = list(machine[r-1][colmin:colmax])
                for i in range(len(array)):
                    if array[i] == "*":
                        gear_pos[(r-1, colmin+i)].append(int(number))
                array = list(machine[r][colmin:colmax])
                for i in range(len(array)):
                    if array[i] == "*":
                        gear_pos[(r, colmin+i)].append(int(number))

                array = list(machine[r+1][colmin:colmax])
                for i in range(len(array)):
                    if array[i] == "*":
                        gear_pos[(r+1, colmin+i)].append(int(number))

            number = ""
for array in gear_pos.values():
    if len(array) == 2:
        summer += array[0]*array[1]
print(summer)