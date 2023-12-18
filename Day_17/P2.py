
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
    last_dir = (node[2]-last_node[2], node[3]-last_node[3])
    return last_dir

def get_path(previous_map, goal):
    curr = goal
    nodes = []
    while curr != (0,10,0,0,(0,1)) and curr != (0,10,0,0,(1,0)):
        print(curr)
        nodes.append((curr[2], curr[3]))
        curr = previous_map[curr]
    #print(curr)
    #print()
    return nodes


possible_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
def traverse():
    goal = (len(costmap)-1, len(costmap[0])-1)
    q = []
    gcost = defaultdict(lambda: math.inf)
    previous = defaultdict(lambda: -1)
    start = (0,10,0,0,(0,1))
    gcost[start] = 0
    heappush(q, (0, start))
    start2 = (0,10,0,0,(1,0))
    gcost[start2] = 0
    heappush(q, (0, start2))
    previous[start] = (-1,11,0,-1,(0,1))
    previous[start2] = (-1,11,-1,0,(1,0))
    while q:
        prio, curr = heappop(q)
        steps_taken, max_steps, row, col, _ = curr

        for dir in possible_dirs:
            new_row = row + dir[0]
            new_col = col + dir[1]
            
            if 0<=new_row<len(costmap) and 0<=new_col<len(costmap[0]):
                tentative_score = gcost[curr] + costmap[new_row][new_col]
                last_dir = get_last_dir(previous, curr)
                new_step = 10 if dir != last_dir else max_steps-1
                new_steps_taken = 1 if dir != last_dir else steps_taken+1
                new_node = (new_steps_taken, new_step, new_row, new_col, dir)

                if (dir==last_dir and new_step<=0 or last_dir==(-dir[0], -dir[1]) or steps_taken<4 and dir!=last_dir):
                    continue
                if tentative_score < gcost[new_node]:
                    previous[new_node] = curr
                    gcost[new_node] = tentative_score
                    guess = tentative_score
                    heappush(q, (guess, new_node))

    def cost_sort(x):
        return gcost[x]
    goal_nodes = [x for x in gcost.keys() if x[2] == goal[0] and x[3] == goal[1] and x[0] >= 4]
    goal_nodes.sort(key=cost_sort)
    curr = goal_nodes[0]
    #path = get_path(previous, curr)
    return "path", gcost[curr]


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
#     print(row)
# print(new_cost)
print(goal_cost)

print(time.time()-t1)