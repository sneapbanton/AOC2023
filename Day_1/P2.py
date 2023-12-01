
data = open("test.txt")
data = open("data.txt")

numnum = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

summ = 0
for line in data:
    earliest_substring = len(line) +2
    es = ""
    latest_substring = len(line) +2
    ls = ""
    for num in numnum:
        index = str.find(line, num)
        if index < earliest_substring and index != -1:
            earliest_substring = index
            es = num
        rev_index = str.find(line[::-1], num[::-1]) - 1
        if rev_index < latest_substring and rev_index > -1:
            latest_substring = rev_index
            print("latest", latest_substring)
            ls = num

    number = ""
    for i in range(len(line)):
        char = line[i]
        if i < earliest_substring:
            if str.isnumeric(char):
                number += char
                break
        else:
            print("es",es)
            number = str(numnum[es])
            break

    for i in range(len(line)):
        rev_line = line[::-1]
        char = rev_line[i]
        if (line == "4nineeightseven2\n"):
            print("Char,", char)
            print(i)
            print(latest_substring)
            print("-----")
        print("line rev", line[::-1])
        print(char)
        if i <= latest_substring:
            if str.isnumeric(char):
                print("adding char", char)
                print("i", i)
                number += char
                break
        else:
            print("ls", ls)
            number += str(numnum[ls])
            break

    print("new number", int(number))
    summ += int(number)
print(summ)