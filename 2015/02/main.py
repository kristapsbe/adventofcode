import math

with open("input.txt", "r") as f:
    data = [[int(c) for c in l.strip().split("x")] for l in f.readlines()]

p1 = 0
p2 = 0
for r in data:
    sides = [r[0] * r[1], r[1] * r[2], r[2] * r[0]]
    p1 += 2 * sum(sides) + min(sides)
    p2 += 2 * (sum(r) - max(r)) + math.prod(r)
print(p1)
print(p2)
