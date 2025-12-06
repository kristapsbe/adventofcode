with open("input.txt", "r") as f:
    data = [[int(c) for c in l.strip().split()] for l in f.readlines()]

p1 = sum([max(l)-min(l) for l in data])
print(p1)

p2 = 0
for l in data:
    total = len(l)
    hit = False
    for i in range(total):
        for j in range(i+1, total):
            if l[i] % l[j] == 0:
               hit = True
               p2 += l[i] / l[j]
               break
            if l[j] % l[i] == 0:
                hit = True
                p2 += l[j] / l[i]
                break
        if hit:
            break
print(int(p2))
