pos = 50
p1 = 0
p2 = 0

with open("input.txt", "r") as f:
    for l in f:
        dir = l[0]
        dist = int(l[1:])

        # TODO: fix so that I don't have to iterate
        # if l[0] == "L":
        #     pos -= int(l[1:])
        # else:
        #     pos += int(l[1:])
        # p2 += abs(pos // 100)

        for _ in range(dist):
            if l[0] == "L":
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
