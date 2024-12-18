size = 70
s = (0, 0)
e = (size, size)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

input = [(int(l.strip().split(",")[0]), int(l.strip().split(",")[1])) for l in open("input.txt", "r")]
walls = input[:12]
walls += [(-1, i) for i in range(-1, size+2)]
walls += [(i, -1) for i in range(size+1)]
walls += [(size+1, i) for i in range(-1, size+2)]
walls += [(i, size+1) for i in range(size+1)]

def draw():
    for i in range(-1, size+2):
        p = ""
        for j in range(-1, size+2):
            if (j, i) in walls:
                p += "#"
            else:
                p += "."
        print(p)

#print(input)
#print(walls)
#draw()

visited = {s: 0}
to_visit = [[(s[0]+d[0], s[1]+d[1]), 1] for d in dirs if (s[0]+d[0], s[1]+d[1]) not in walls]
while len(to_visit) > 0:
    tmp_to_visit = []
    for n in to_visit:
        for d in dirs:
            nn = (n[0][0]+d[0], n[0][1]+d[1])
            np = n[1]+1
            if nn not in walls and (nn not in visited or visited[nn] > np):
                visited[nn] = np
                tmp_to_visit.append([nn, np])
    to_visit = tmp_to_visit

print(visited[e])


visited = {s: 0, e: 0}
ct = 1024
while e in visited: # very dumb and very slow - should figure out set of potential problem nodes
    ct += 1
    #print(ct)
    walls = input[:ct]
    walls += [(-1, i) for i in range(-1, size+2)]
    walls += [(i, -1) for i in range(size+1)]
    walls += [(size+1, i) for i in range(-1, size+2)]
    walls += [(i, size+1) for i in range(size+1)]
    visited = {s: 0}
    to_visit = [[(s[0]+d[0], s[1]+d[1]), 1] for d in dirs if (s[0]+d[0], s[1]+d[1]) not in walls]

    while len(to_visit) > 0:
        tmp_to_visit = []
        for n in to_visit:
            for d in dirs:
                nn = (n[0][0]+d[0], n[0][1]+d[1])
                np = n[1]+1
                if nn not in walls and (nn not in visited or visited[nn] > np):
                    visited[nn] = np
                    tmp_to_visit.append([nn, np])
        to_visit = tmp_to_visit

print(input[ct-1])
