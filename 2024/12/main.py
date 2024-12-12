grid = [list(r.strip()) for r in open("input.txt", "r").readlines()]

h = len(grid)
w = len(grid[0])
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
visited = []
areas = {}
fences = {}

def flood_fill(e, i, j):
    visited.append((i, j))
    areas[e][-1].append((i, j))

    n_fences = 4
    for d in dirs:
        ni = i+d[0]
        nj = j+d[1]
        if ni >= 0 and ni < h and nj >= 0 and nj < w and e == grid[ni][nj]:
            n_fences -= 1
            if (ni, nj) not in visited:
                flood_fill(e, ni, nj)
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
