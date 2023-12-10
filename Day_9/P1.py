
data = open("test.txt")
data = open("data.txt")


def extrapolate(nums):
    new_nums = []
    for i in range(len(nums)-1):
        new_nums.append(int(nums[i+1]) - int(nums[i]))
    if set(new_nums) == set([0]):
        return 0
    new_num = extrapolate(new_nums)
    return new_nums[-1] + new_num


summary_extrapolate = 0

for line in data:
    line = line.strip("\n")
    nums = line.split(" ")
    extra_num = extrapolate(nums)
    summary_extrapolate += int(nums[-1]) + extra_num

print(summary_extrapolate)