pos = 50
p1 = 0
p2 = 0

with open("input.txt", "r") as f:
    for i, l in enumerate(f):
        dir = l[0]
        dist = int(l[1:])

        # full circles
        p2 += dist // 100
        dist %= 100

        if dir == "L":
            new_pos = pos - dist
        else:
            new_pos = pos + dist

        if (new_pos <= 0 and pos != 0) or new_pos >= 100:
            p2 += 1

        pos = new_pos % 100
        if pos == 0:
            p1 += 1

print(p1)
print(p2)
