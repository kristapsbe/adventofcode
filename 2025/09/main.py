with open("input.txt", "r") as f:
    data = [[int(c) for c in l.strip().split(",")] for l in f.readlines()]

num_coords = len(data)


p1 = 0
for i in range(num_coords):
    for j in range(i + 1, num_coords):
        curr_rect = (abs(data[i][0] - data[j][0]) + 1) * (
            abs(data[i][1] - data[j][1]) + 1
        )
        p1 = max(curr_rect, p1)
print(p1)

p2 = 0
