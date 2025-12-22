with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read().strip()

pos = (0, 0)
p1 = {pos: 1}
p2 = {pos: 2}
santapos = (0, 0)
robopos = (0, 0)

deltas = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

for i, d in enumerate(data):
    tmp = (pos[0] + deltas[d][0], pos[1] + deltas[d][1])
    if tmp not in p1:
        p1[tmp] = 0
    p1[tmp] += 1
    pos = tmp

    if i % 2 == 0:
        tmpp2 = (santapos[0] + deltas[d][0], santapos[1] + deltas[d][1])
    else:
        tmpp2 = (robopos[0] + deltas[d][0], robopos[1] + deltas[d][1])

    if tmpp2 not in p2:
        p2[tmpp2] = 0
    p2[tmpp2] += 1

    if i % 2 == 0:
        santapos = tmpp2
    else:
        robopos = tmpp2

print(len(p1))
print(len(p2))
