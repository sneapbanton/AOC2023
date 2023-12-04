
data = open("test.txt")
data = open("data.txt")

points = 0

for line in data:
    card = line.strip("\n")
    card = card[card.index(":")+1:]
    card = card.split("|")
    winning_numbers = set(card[0].split(" "))
    my_numbers = set(card[1].split(" "))
    winning_numbers.remove("")
    n = len(winning_numbers.intersection(my_numbers))
    if (n):
        points += (2**(n-1))

print(points)
