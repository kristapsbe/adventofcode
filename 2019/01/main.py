with open("input.txt", "r") as f:
    nums = [int(l.strip()) for l in f.readlines()]

p1 = sum([n // 3 - 2 for n in nums])
print(p1)

p2 = 0
for n in nums:
    tmp = n // 3 - 2
    while tmp > 0:
        p2 += tmp
        tmp = tmp // 3 - 2
print(p2)
