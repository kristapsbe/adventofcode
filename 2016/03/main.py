with open("input.txt", "r", encoding="utf-8") as f:
    data = [[int(c) for c in l.strip().split()] for l in f.readlines()]

p1 = 0
for d in data:
    tmp = sum(d)
    if all([tmp - d[i] > d[i] for i in range(3)]):
        p1 += 1
print(p1)

p2_data = [
    [data[(i * 3) + k][j] for k in range(3)]
    for i in range(len(data) // 3)
    for j in range(3)
]
p2 = 0
for d in p2_data:
    tmp = sum(d)
    if all([tmp - d[i] > d[i] for i in range(3)]):
        p2 += 1
print(p2)
