
from collections import defaultdict
from heapq import heappush, heappop
import math
import time

data = open("test.txt")
data = open("data.txt")

costmap = []
for line in data:
    costmap.append([int(x) for x in list(line.strip("\n"))])

t1 = time.time()

def get_last_dir(previous_map, node):
    last_node = previous_map[node]
    last_dir = (node[1]-last_node[1], node[2]-last_node[2])
    return last_dir

def get_path(previous_map, goal):
    curr = goal
    nodes = []
    while curr != (3,0,0,(0,1)):
        print(curr)
        nodes.append((curr[1], curr[2]))
        curr = previous_map[curr]
    print(curr)
    print()
    return nodes


possible_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
def traverse():
    goal = (len(costmap)-1, len(costmap[0])-1)
    q = []
    gcost = defaultdict(lambda: math.inf)
    previous = defaultdict(lambda: -1)
    start = (3,0,0,(0,1))
    gcost[start] = 0
    heappush(q, (0, start))
    previous[start] = (4,0,-1,(0,1))
    while q:
        prio, curr = heappop(q)
        steps, row, col, _ = curr

        for dir in possible_dirs:
            new_row = row + dir[0]
            new_col = col + dir[1]
            
            if 0<=new_row<len(costmap) and 0<=new_col<len(costmap[0]):
                tentative_score = gcost[curr] + costmap[new_row][new_col]
                last_dir = get_last_dir(previous, curr)
                new_step = 3 if dir != last_dir else steps-1
                new_node = (new_step, new_row, new_col, dir)
                if (dir==last_dir and new_step<=0 or last_dir==(-dir[0], -dir[1])):
                    continue
                if tentative_score < gcost[new_node]:
                    previous[new_node] = curr
                    gcost[new_node] = tentative_score
                    guess = tentative_score
                    heappush(q, (guess, new_node))

    def cost_sort(x):
        return gcost[x]
    goal_nodes = [x for x in gcost.keys() if x[1] == goal[0] and x[2] == goal[1]]
    goal_nodes.sort(key=cost_sort)
    curr = goal_nodes[0]
    #path = get_path(previous, curr)
    return "", gcost[curr]


path, goal_cost = traverse()

# new_cost = 0
# for r in range(len(costmap)):
#     row = ""
#     for c in range(len(costmap[0])):
#         if (r,c) not in path:
#             row += "."
#         else:
#             row += "#"
#             new_cost += costmap[r][c]
    #print(row)
#print(new_cost)
print(goal_cost)

print(time.time()-t1)