with open("input.txt", "r") as f:
    data = [l.strip().split(" ") for l in f.readlines()]

data = [[e[0], int(e[1])] for e in data]
pos = [0, 0]
pos2 = [0, 0]
aim = 0

for d in data:
    match d[0]:
        case "forward":
            pos[1] += d[1]
            pos2[1] += d[1]
            pos2[0] += aim*d[1]
        case "down":
            pos[0] += d[1]
            aim += d[1]
        case "up":
            pos[0] -= d[1]
            aim -= d[1]
print(pos[0]*pos[1])
print(pos2[0]*pos2[1])
