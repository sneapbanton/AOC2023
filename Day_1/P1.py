
data = open("test.txt")
data = open("data.txt")

summ = 0
for line in data:
    number = ""
    for char in line:
        if str.isnumeric(char):
            number += char
    if len(number) > 1:
        newnumber = number[0:1] + number[-1]
        print("int(number)", int(newnumber))
        
    elif (len(number) == 1):
        newnumber = number[0] + number[0]
    summ += int(newnumber)
print(summ)