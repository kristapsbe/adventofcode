input = [list(l.strip()) for l in open("input.txt", "r").readlines()]

h = len(input)
w = len(input[0])
antennas = {}
for i in range(h):
    for j in range(w):
        if input[i][j] != ".":
            if input[i][j] not in antennas:
                antennas[input[i][j]] = []
            antennas[input[i][j]].append((i, j))

antinodes = []
for _,v in antennas.items():
    for i in range(len(v)-1):
        for j in range(i+1, len(v)):
            di = v[i][0]-v[j][0]
            dj = v[i][1]-v[j][1]
            ni = v[i][0]+di
            nj = v[i][1]+dj
            if ni >= 0 and ni < h and nj >= 0 and nj < w:
                antinodes.append((ni, nj))
            ni = v[j][0]-di
            nj = v[j][1]-dj
            if ni >= 0 and ni < h and nj >= 0 and nj < w:
                antinodes.append((ni, nj))
print(len(set(antinodes)))


antinodes = []
for _,v in antennas.items():
    antinodes += v
    for i in range(len(v)-1):
        for j in range(i+1, len(v)):
            di = v[i][0]-v[j][0]
            dj = v[i][1]-v[j][1]
            ni = v[i][0]+di
            nj = v[i][1]+dj
            while ni >= 0 and ni < h and nj >= 0 and nj < w:
                antinodes.append((ni, nj))
                ni += di
                nj += dj
            ni = v[j][0]-di
            nj = v[j][1]-dj
            while ni >= 0 and ni < h and nj >= 0 and nj < w:
                antinodes.append((ni, nj))
                ni -= di
                nj -= dj

print(len(set(antinodes)))
