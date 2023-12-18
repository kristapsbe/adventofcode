# https://adventofcode.com/2023/day/18


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/18/input
    lines = [l.strip().split(" ") for l in f.read().split("\n") if l.strip() != ""]

dirs = []
for l in lines:
    dirs.append([l[0], int(l[1]), l[2]])

digs = {}
moves = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
ci = 0
cj = 0
for d in dirs:
    for _ in range(d[1]):
        ci += moves[d[0]][0]
        cj += moves[d[0]][1]
        digs[(ci, cj)] = [d[0], d[2][1:-1]]

i_vals = [d[0] for d in digs.keys()]
j_vals = [d[1] for d in digs.keys()]
min_i = min(i_vals)
min_j = min(j_vals)
max_i = max(i_vals)
max_j = max(j_vals)

h = max_i-min_i+1
w = max_j-min_j+1

dig_map = [["." if (i+min_i, j+min_j) not in digs else digs[(i+min_i, j+min_j)][0] for j in range(w)] for i in range(h)]
#print(digs)

#for d in dig_map:
#    print(d)

filled_dig_map = [["." for j in range(w)] for i in range(h)]
ct = 0
for i in range(h):
    dig_ct = 0
    for j in range(w):
        if dig_map[i][j] != ".":
            ct += 1
            filled_dig_map[i][j] = "#"
            if dig_map[i][j] in ("U", "D"):
                dig_ct += 1
        elif dig_ct%2 == 1:
            ct += 1
            filled_dig_map[i][j] = "#"

#print()
#for d in filled_dig_map:
#    print(d)
            
# TODO: https://en.wikipedia.org/wiki/Pick's_theorem
print(ct)