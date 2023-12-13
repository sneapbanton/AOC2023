from copy import copy 
data = open("test.txt")
data = open("data.txt")


def spring_brute_force(spring: str, nums):
    if "?" in spring:
        i = spring.index("?")
        spring = list(spring)
        spring[i] = "."
        result = spring_brute_force(''.join(copy(spring)), nums)
        spring[i] = "#"
        result += spring_brute_force(''.join(copy(spring)), nums)
        return result
    else:
        groups = spring.split(".")
        groups = [len(x) for x in groups if x]
        if len(groups) != len(nums):
            return 0
        for i in range(len(groups)):
            if groups[i] != nums[i]:
                return 0
        return 1

big_res = 0
lines_handled = 0
for line in data:
    line = line.strip("\n")
    springs, nums = line.split(" ")
    nums = [int(x) for x in nums.split(",")]
    big_res += spring_brute_force(springs, nums)

    lines_handled += 1
    print(lines_handled)

print(big_res)
