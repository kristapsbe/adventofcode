lists = []
with open("input.txt", "r") as f:
    lists = [[int(i) for i in l.strip().split("   ")] for l in f.readlines()]
first, second = list(zip(*lists))

print(f"PART ONE: {sum([abs(f-s) for f, s in zip(sorted(first), sorted(second))])}")
print(f"PART TWO: {sum([f*second.count(f) for f in set(first)])}")
