min_save = 100
cheat = 2
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

s = (0, 0)
e = (0, 0)
path = []
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
    for i in range(len(lines)):
        if "S" in lines[i]:
            s = (i, lines[i].index("S"))
        if "E" in lines[i]:
            e = (i, lines[i].index("E"))

    p = s
    path.append(p)
    while p != e:
        for d in dirs:
            if lines[p[0]+d[0]][p[1]+d[1]] in [".", "E"] and (p[0]+d[0], p[1]+d[1]) not in path:
                p = (p[0]+d[0], p[1]+d[1])
                path.append(p)
                break

ct = 0
for i in range(len(path)-min_save):
    for j in range(i+min_save, len(path)):
        if abs(path[i][0]-path[j][0])+abs(path[i][1]-path[j][1]) <= cheat:
            if j-i-(abs(path[i][0]-path[j][0])+abs(path[i][1]-path[j][1])) >= min_save:
                ct += 1
print(ct)
cheat = 20
ct = {}
for i in range(len(path)-min_save):
    for j in range(i+min_save, len(path)):
        if (i, j) not in ct and abs(path[i][0]-path[j][0])+abs(path[i][1]-path[j][1]) <= cheat:
            dst = j-i-(abs(path[i][0]-path[j][0])+abs(path[i][1]-path[j][1]))
            if dst >= min_save:
                ct[(i, j)] = dst
print(len(ct))
