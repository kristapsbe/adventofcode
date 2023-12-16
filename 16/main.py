# https://adventofcode.com/2023/day/16


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/16/input
    lines = [l.strip() for l in f.read().split("\n") if l.strip() != ""]


h = len(lines)
w = len(lines[0])

# PART ONE
def count_energ(beams):
    energ = [[[] for _ in range(w)] for _ in range(h)]
    while len(beams) > 0:
        tmp = []
        for b in beams:
            ni = b[0]+b[2]
            nj = b[1]+b[3]
            if ni < 0 or nj < 0 or ni >= h or nj >= w or ((b[2], b[3]) in energ[ni][nj]):
                continue
            energ[ni][nj].append((b[2], b[3]))
            nc = lines[ni][nj]
            if b[3] != 0: # moving horizontally
                if nc == "|":
                    tmp.append((ni, nj, 1, 0))
                    tmp.append((ni, nj, -1, 0))
                elif nc == "/":
                    if b[3] == 1:
                        tmp.append((ni, nj, -1, 0))
                    else:
                        tmp.append((ni, nj, 1, 0))
                elif nc == "\\":
                    if b[3] == 1:
                        tmp.append((ni, nj, 1, 0))
                    else:
                        tmp.append((ni, nj, -1, 0))
                else:
                    tmp.append((ni, nj, b[2], b[3]))
            else: # moving vertically
                if nc == "-":
                    tmp.append((ni, nj, 0, 1))
                    tmp.append((ni, nj, 0, -1))
                elif nc == "/":
                    if b[2] == 1:
                        tmp.append((ni, nj, 0, -1))
                    else:
                        tmp.append((ni, nj, 0, 1))
                elif nc == "\\":
                    if b[2] == 1:
                        tmp.append((ni, nj, 0, 1))
                    else:
                        tmp.append((ni, nj, 0, -1))
                else:
                    tmp.append((ni, nj, b[2], b[3]))
        beams = tmp
    return energ

ct = 0
for e in count_energ([(0, -1, 0, 1)] ):
    ct = ct+sum([1 for t in e if len(t) > 0])
print(f"PART ONE: {ct}")


# TODO: I'm re-treading paths I've already checked - would recursion work better? (would let me cache total value of path and reuse it later)
# PART TWO
cts = []
for i in range(h):
    ct = 0
    for e in count_energ([(i, -1, 0, 1)] ):
        ct = ct+sum([1 for t in e if len(t) > 0])
    cts.append(ct)

    ct = 0
    for e in count_energ([(i, w, 0, -1)] ):
        ct = ct+sum([1 for t in e if len(t) > 0])
    cts.append(ct)

for j in range(w):
    ct = 0
    for e in count_energ([(-1, j, 1, 0)] ):
        ct = ct+sum([1 for t in e if len(t) > 0])
    cts.append(ct)

    ct = 0
    for e in count_energ([(h, j, -1, 0)] ):
        ct = ct+sum([1 for t in e if len(t) > 0])
    cts.append(ct)

print(f"PART TWO: {max(cts)}")