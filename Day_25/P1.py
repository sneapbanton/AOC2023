from networkx import Graph, minimum_cut
from itertools import combinations

data = open("test.txt")
data = open("data.txt")

groph = Graph()
for line in data:
    key, values = line.strip("\n").split(":")
    values = values.split(" ")
    for val in values[1:]:
        groph.add_edge(key,val,capacity=1)

for start,end in combinations(groph.nodes, 2):
    cut, parts = minimum_cut(groph, start, end)
    if cut == 3:
        print(len(parts[0])*len(parts[1]))
        break