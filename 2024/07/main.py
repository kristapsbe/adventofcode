input = [[int(l.split(":")[0]), [int(e) for e in l.split(":")[1].strip().split(" ")]] for l in open("input.txt", "r").readlines()]

def solve_first(nums, total, target):
    if len(nums) == 0:
        return total == target
    else:
        return solve_first(nums[1:], total+nums[0], target) or solve_first(nums[1:], total*nums[0], target)

res = []
for e in input:
    if solve_first(e[1][1:], e[1][0], e[0]):
        res.append(e[0])
print(sum(res))

def solve_second(nums, total, target):
    if len(nums) == 0:
        return total == target
    else:
        return solve_second(nums[1:], total+nums[0], target) or solve_second(nums[1:], total*nums[0], target) or solve_second(nums[1:], int(f"{total}{nums[0]}"), target)

res = []
for e in input:
    if solve_second(e[1][1:], e[1][0], e[0]):
        res.append(e[0])
print(sum(res))
