from collections import defaultdict

data = open("test.txt")
data = open("data.txt")

def def_value(): 
    return 1
      
# Defining the dict 
cards = defaultdict(def_value) 

card_ids = []
for line in data:
    card = line.strip("\n")
    id = int(card.split(":")[0].split(" ")[-1])
    card = card[card.index(":")+1:]
    card = card.split("|")
    winning_numbers = set(card[0].split(" "))
    my_numbers = set(card[1].split(" "))
    winning_numbers.remove("")
    n = len(winning_numbers.intersection(my_numbers))
    for i in range(1,n+1):
        cards[id+i] = cards[id+i] + cards[id]

    card_ids.append(id)
    print(cards)
    

n = 0
for x in card_ids:
    n += cards[x]

print(n)
