grid = [list(r.strip()) for r in open("input.txt", "r").readlines()]

h = len(grid)
w = len(grid[0])
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
o_dirs = [(-1, 0), (0, -1)]

visited = []
areas = {}
fences = {}


def find_fence_dirs(e, i, j):
    f_dirs = []
    for d in dirs:
        ni = i+d[0]
        nj = j+d[1]
        if ni < 0 or ni >= h or nj < 0 or nj >= w or e != grid[ni][nj]:
            f_dirs.append(d)
    return f_dirs


def flood_fill(e, i, j, part_two=False):
    visited.append((i, j))
    areas[e][-1].append((i, j))

    n_fences = 4
    c_dirs = find_fence_dirs(e, i, j) # part two
    for d in dirs:
        ni = i+d[0]
        nj = j+d[1]
        if ni >= 0 and ni < h and nj >= 0 and nj < w and e == grid[ni][nj]:
            n_fences -= 1
            if part_two:
                if d in o_dirs:
                    n_fences -= len([o for o in find_fence_dirs(e, ni, nj) if o in c_dirs])

            if (ni, nj) not in visited:
                flood_fill(e, ni, nj, part_two)
    fences[e][-1] += n_fences

for i in range(h):
    for j in range(w):
        if (i, j) not in visited:
            e = grid[i][j]

            if e not in areas:
                areas[e] = []
                fences[e] = []

            areas[e].append([])
            fences[e].append(0)
            flood_fill(e, i, j)

ct = 0
for k, v in areas.items():
    for i in range(len(v)):
        ct += len(v[i])*fences[k][i]
print(ct)

visited = []
areas = {}
fences = {}

for i in range(h):
    for j in range(w):
        if (i, j) not in visited:
            e = grid[i][j]

            if e not in areas:
                areas[e] = []
                fences[e] = []

            areas[e].append([])
            fences[e].append(0)
            flood_fill(e, i, j, True)

ct = 0
for k, v in areas.items():
    for i in range(len(v)):
        ct += len(v[i])*fences[k][i]
print(ct)
