with open("input.txt", "r") as f:
    data = [int(l.strip()) for l in f.readlines()]

p1 = 0
for i in range(len(data)):
    for j in range(i, len(data)):
        if data[i] + data[j] == 2020:
            p1 = data[i] * data[j]
    if p1 != 0:
        break
print(p1)

p2 = 0
for i in range(len(data)):
    for j in range(i, len(data)):
        for k in range(j, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                p2 = data[i] * data[j] * data[k]
    if p2 != 0:
        break
print(p2)
