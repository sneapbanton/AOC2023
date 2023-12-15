from collections import defaultdict

data = open("test.txt")
data = open("data.txt")

box = defaultdict(lambda: defaultdict(lambda: 0))
box_order = defaultdict(lambda: [])

def calculate_hash(word):
    current_val = 0
    for char in list(word):
        current_val += ord(char)
        current_val = current_val * 17
        current_val = current_val % 256
    return current_val

def put_into_box(word):
    if "-" in word:
        box_num = calculate_hash(word[:-1])
        box[box_num][word[:-1]] = 0
        if word[:-1] in box_order[box_num]:
            box_order[box_num].pop(box_order[box_num].index(word[:-1]))
    else:
        label, num = word.split("=")
        box_num = calculate_hash(label)
        box[box_num][label] = num
        if label not in box_order[box_num]:
            box_order[box_num].append(label)

for line in data:
    strings = line.strip("\n").split(",")

for word in strings:
    res = put_into_box(word)

big_res = 0
for i in range(256):
    for j, label in enumerate(box_order[i]):
        res = (i+1)*(j+1)*int(box[i][label])
        print(res)
        big_res += res

print(big_res)