from collections import Counter, defaultdict
import re

data = open("test.txt")
data = open("data.txt")

def empty_array():
    return []

hands = []
bids = []

sorted_hands = defaultdict(empty_array)

def sort_hand(hand: str, i: int):
    res = Counter(hand)
    vals = []

    if "J" in hand and set("J") != set(hand):
        max_key = -1
        for key in res:
            if key != "J" and (max_key == -1 or res[key] > res[max_key]):
                max_key = key

        new_hand = hand.replace("J", max_key)
        res = Counter(new_hand)

    for char in set(res.elements()):
        vals.append(res[char])
    

    if 5 in vals:
        sorted_hands["five"].append(i)
    elif 4 in vals:
        sorted_hands["four"].append(i)
    elif 3 in vals and 2 in vals:
        sorted_hands["house"].append(i)
    elif 3 in vals:
        sorted_hands["three"].append(i)
    elif Counter(vals)[2] == 2: # two pairs
        sorted_hands["twop"].append(i)
    elif 2 in vals:
        sorted_hands["pair"].append(i)
    else:
        sorted_hands["high"].append(i)


def order_within_type(hand_types):
    subord_list = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    order_dict = {}
    for i in range(len(subord_list)):
        order_dict[subord_list[i]] = i

    sorted_hands = sorted(hand_types, key=lambda x: [order_dict[char] if char in order_dict else int(char) for char in re.findall(r'\D|\d', hands[x])])
    return sorted_hands


for line in data:
    line = line.strip("\n")
    data = line.split(" ")
    hands.append(data[0])
    bids.append(int(data[1]))


for i in range(len(hands)):
    hand = hands[i]
    sort_hand(hand, i)

for i in sorted_hands:
    print(i)
    new_order = order_within_type(sorted_hands[i])
    sorted_hands[i] = new_order
    
rank = 1
winnings = 0
rankings = [sorted_hands["five"], sorted_hands["four"], sorted_hands["house"], sorted_hands["three"], sorted_hands["twop"], sorted_hands["pair"], sorted_hands["high"]]
rankings.reverse()
for type in rankings:
    type.reverse()
    for h in type:
        print("Rank,", rank, ":", hands[h])
        winnings += rank * bids[h]
        rank += 1


print(winnings)