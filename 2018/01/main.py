with open("input.txt", "r") as f:
    nums = [int(l.strip()) for l in f.readlines()]

p1 = sum(nums)
print(p1)

seen = set([0])
i = 0
p2 = 0
total = len(nums)
while True:
    p2 += nums[i % total]
    i += 1
    if p2 in seen:
        break
    seen.add(p2)
print(p2)
