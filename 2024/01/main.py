lists = []
with open("input.txt", "r") as f:
    lists = [[int(i) for i in l.strip().split("   ")] for l in f.readlines()]
first = sorted([e[0] for e in lists])
second = sorted([e[1] for e in lists])

print(sum([abs(first[i]-second[i]) for i in range(len(first))]))

print(sum([f*second.count(f) for f in set(first)]))
