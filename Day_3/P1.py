
data = open("test.txt")
data = open("data.txt")

machine = []

for line in data:
    line = str.strip(line, "\n")
    machine.append("." + line + ".")

empty_row = len(machine[0])*"."
machine.insert(0, empty_row)
machine.append(empty_row)

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

                array += list(machine[r-1][colmin:colmax])
                array += list(machine[r][colmin:colmax])
                array += list(machine[r+1][colmin:colmax])
                s = set(array)
                symbols = [x for x in s if not str.isnumeric(x) and x and x != "."]
                if symbols:
                    summer += int(number)
            number = ""
            

print(summer)