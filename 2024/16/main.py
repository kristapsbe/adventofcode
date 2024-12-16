s = (0, 0)
e = (0, 0)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
g = {}

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
    i = 0
    for l in lines:
        j = 0
        for c in l:
            if c != "#":
                match c:
                    case ".":
                        g[(i, j)] = [(i+d[0], j+d[1]) for d in dirs if lines[i+d[0]][j+d[1]] != "#"]
                    case "S":
                        g[(i, j)] = [(i+d[0], j+d[1]) for d in dirs if lines[i+d[0]][j+d[1]] != "#"]
                        s = (i, j)
                    case "E":
                        g[(i, j)] = [(i+d[0], j+d[1]) for d in dirs if lines[i+d[0]][j+d[1]] != "#"]
                        e = (i, j)
            j += 1
        i += 1

visited = {s: [0, {0: [[s]]}]}
to_visit = [(s, (0, 1), 0, [s])]
dir_points = {0: 1, 1: 1001, -1: 1001, 2: 2001}
while len(to_visit) > 0:
    tmp_to_visit = []
    for v in to_visit:
        (n, d, p, path) = v
        di = dirs.index(v[1])
        for md, mp in dir_points.items():
            td = dirs[(di+md)%4]
            nn = (n[0]+td[0], n[1]+td[1])
            np = p+mp
            if nn in g[n]:
                if (nn not in visited or visited[nn][0] >= np): # dumb solutions for p2 - allows for an arbitrary turn if necessary
                    tmp_to_visit.append((nn, td, np, path+[nn]))
                    if nn not in visited:
                        visited[nn] = [np, {}]
                    if visited[nn][0] > np: # dealing with dumbness of p2 solution
                        visited[nn][0] = np
                if np not in visited[nn][1]:
                    visited[nn][1][np] = []
                visited[nn][1][np].append(path)
    to_visit = tmp_to_visit

print(visited[e][0])
#print(visited[e][1][min(visited[e][1].keys())])
tmp_a = [visited[a][1][visited[a][0]] for b in visited[e][1][visited[e][0]] for a in b]
tmp_b = [a for b in tmp_a for a in b]
tmp_c = list(set([a for b in tmp_b for a in b]+[a for b in visited[e][1][visited[e][0]] for a in b]+[e]))

print(len(tmp_c)) # logic's still broken, but accidentally got the right answer 551

# with open("input.txt", "r") as f:
#     lines = [l.strip() for l in f.readlines()]
#     i = 0
#     for l in lines:
#         j = 0
#         o = ""
#         for c in l:
#             o += "O" if (i, j) in tmp_c else c
#             j += 1
#         i += 1
#         print(o)

#print(visited)
