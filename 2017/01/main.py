with open("input.txt", "r") as f:
    nums = [int(c) for c in f.read().strip()]

p1 = 0
p2 = 0
half = len(nums) // 2
for i in range(len(nums)):
    if nums[i - 1] == nums[i]:
        p1 += nums[i]
    if nums[i - half] == nums[i]:
        p2 += nums[i]
print(p1)
print(p2)
