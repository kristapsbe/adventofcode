with open("input.txt", "r") as f:
    data = [int(l.strip()) for l in f.readlines()]

p1 = 0
for i in range(1, len(data)):
    if data[i - 1] < data[i]:
        p1 += 1
print(p1)

p2 = 0
for i in range(4, len(data) + 1):
    if sum(data[i - 4 : i - 1]) < sum(data[i - 3 : i]):
        p2 += 1
print(p2)
