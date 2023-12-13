from copy import copy 
from functools import cache
data = open("test.txt")
data = open("data.txt")

@cache
def spring_brute_force(spring, nums, prev):
    a = set()
    if (not spring or set(spring).issubset(set([".", "?"]))) and (not nums or (len(nums)==1 and nums[0] == 0)):
        return 1
    
    if not spring and (len(nums)==1 and nums[0]>0 or len(nums)>1):
        return 0

    if spring and set(spring)!=set(".") and not nums:
        return 0

    new_prev = spring[0]
    if prev == ".":
        if nums[0] == 0:
            assert False
        if spring[0] == ".":
            return spring_brute_force(spring[1:], nums, new_prev)
        elif spring[0] == "#":
            c_nums = list(copy(nums))
            c_nums[0] = c_nums[0] - 1
            return spring_brute_force(spring[1:], tuple(c_nums), new_prev)
        elif spring[0] == "?":
            c_nums = list(copy(nums))
            c_nums[0] = c_nums[0] - 1
            ways =  spring_brute_force(spring[1:], tuple(c_nums), "#")
            return ways + spring_brute_force(spring[1:], nums, ".")
        else:
            assert False

    elif prev == "#":
        if spring[0] == "." and nums[0] > 0:
            return 0
        elif spring[0] == "." and nums[0] == 0:
            return spring_brute_force(spring[1:], nums[1:], new_prev)
        elif spring[0] == "#" and nums[0] > 0:
            c_nums = list(copy(nums))
            c_nums[0] = c_nums[0] - 1
            return spring_brute_force(spring[1:], tuple(c_nums), new_prev)
        elif spring[0] == "#" and nums[0] == 0:
            return 0
        elif spring[0] == "?" and nums[0] > 0:
            c_nums = list(copy(nums))
            c_nums[0] = c_nums[0] - 1
            return spring_brute_force(spring[1:], tuple(c_nums), "#")
        elif spring[0] == "?" and nums[0] == 0:
            return spring_brute_force(spring[1:], nums[1:], ".")
        else:
            assert False
    else:
        print(prev)
        assert False

big_res = 0
lines_handled = 0
for line in data:
    line = line.strip("\n")
    springs, nums = line.split(" ")
    springs = ((springs + "?")*5)[:-1]
    nums = [int(x) for x in nums.split(",")]*5
    small_res = spring_brute_force(springs, tuple(nums), ".")
    #print(small_res)
    big_res += small_res

    lines_handled += 1
    print(lines_handled)

print(big_res)
