pos = 50
p1 = 0
p2 = 0

with open("input.txt", "r") as f:
    for i, l in enumerate(f):
        dir = l[0]
        dist = int(l[1:])

        # full circles
        p2 += dist // 100
        dist %= 100  # TODO: there's probs a better way, but this, at least, shortens the loop

        for _ in range(dist):
            if dir == "L":
                pos -= 1
            else:
                pos += 1
            if pos % 100 == 0:
                p2 += 1

        pos %= 100
        if pos == 0:
            p1 += 1

print(p1)
print(p2)
