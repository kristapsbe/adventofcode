map = [list(l.strip()) for l in open("input.txt", "r").readlines()]
obstacles = []

start_dir = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}
next_dir = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}
dir = (0, 0)
positions = []

pos = (0, 0)
for i, row in enumerate(map):
    for j, ch in enumerate(row):
        if ch == "#":
            obstacles.append((i, j))
        elif ch in start_dir:
            dir = start_dir[ch]
            pos = (i, j)


def find_next_obstacle(p, m, obstacles):
    vo = None
    for o in obstacles:
        if (m[0] == 0 and p[0] == o[0] and m[1]*(o[1]-p[1])>0):
            if vo is None or abs(vo[1]-p[1]) > abs(o[1]-p[1]):
                vo = o
        elif (m[1] == 0 and p[1] == o[1] and m[0]*(o[0]-p[0])>0):
            if vo is None or abs(vo[0]-p[0]) > abs(o[0]-p[0]):
                vo = o
    return vo


def calculate_path(p, m, positions, obstacles):
    visited = {}
    while True:
        vo = find_next_obstacle(p, m, obstacles)

        if vo is None:
            positions.append([p, (p[0] if m[0] == 0 else len(map), p[1] if m[1] == 0 else len(map[0])), m])
            break
        else:
            positions.append([p, (vo[0]-m[0], vo[1]-m[1]), m])
            p = positions[-1][1]

            if vo not in visited:
                visited[vo] = []
            if m in visited[vo]:
                return []
            else:
                visited[vo].append(m)

            m = next_dir[m]
    return positions

new_obstacles = []
initial_paths = calculate_path(pos, dir, positions, obstacles)
for p in initial_paths:
    cp = p[0]
    tp = p[1]
    m = p[2]
    while cp[0] != tp[0] or cp[1] != tp[1]:
        map[cp[0]][cp[1]] = "X"
        next_cp = (cp[0]+m[0], cp[1]+m[1])

        pn_m = next_dir[m]
        pn_o = find_next_obstacle(cp, pn_m, obstacles)
        if pn_o is not None:
            new_obstacles.append(next_cp)

        cp = next_cp


print(sum([len([c for c in r if c == "X"]) for r in map]))
# very slow
print(len([o for o in list(set(new_obstacles)) if calculate_path(pos, dir, positions, obstacles+[o]) == []]))
