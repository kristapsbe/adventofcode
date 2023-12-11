# https://adventofcode.com/2023/day/11


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/11/input
    lines = [l.strip() for l in f.read().split("\n") if l.strip() != ""]


def calc_dist(lines, expansion):
    h = len(lines)
    w = len(lines[0])
    r_vals = []
    c_vals = []
    # fake-expand universe
    # do rows
    for r in lines:	
        r_vals.append(expansion if len([c for c in r if c != "."]) == 0 else 1)

    # do cols
    for c in range(w):
        c_vals.append(expansion if len([u[c] for u in lines if u[c] != "."]) == 0 else 1)

    stars = []
    for i in range(h):
        for j in range(w):
            if lines[i][j] == "#":
                stars.append((i, j))

    dists = []
    for i in range(len(stars)):
        for j in range(len(stars)-i-1):
            min_r = min(stars[i][0], stars[i+j+1][0])
            max_r = max(stars[i][0], stars[i+j+1][0])
            min_c = min(stars[i][1], stars[i+j+1][1])
            max_c = max(stars[i][1], stars[i+j+1][1])	
            dists.append(sum(r_vals[min_r:max_r])+sum(c_vals[min_c:max_c]))
    return sum(dists)


# PART ONE
print(calc_dist(lines, 2))

# PART TWO
print(calc_dist(lines, 1000000))
