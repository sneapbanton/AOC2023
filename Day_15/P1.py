
data = open("test.txt")
data = open("data.txt")


def calculate_hash(word):
    current_val = 0
    for char in list(word):
        current_val += ord(char)
        current_val = current_val * 17
        current_val = current_val % 256
    return current_val


for line in data:
    strings = line.strip("\n").split(",")

big_res = 0
for word in strings:
    res = calculate_hash(word)
    big_res += res
print(big_res)