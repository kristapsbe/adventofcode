input = [[int(c) if c != "." else -1 for c in l.strip()] for l in open("input.txt", "r").readlines()]

h = len(input)
w = len(input[0])

def find_trails(i, j, c, r, do_check=True):
    if c == 9:
        if do_check and (i, j) in r:
            return r
        else:
            return r+[(i, j)]
    nc = c+1
    if i-1 >= 0 and input[i-1][j] == nc:
        r = find_trails(i-1, j, nc, r, do_check)
    if i+1 < h and input[i+1][j] == nc:
        r = find_trails(i+1, j, nc, r, do_check)
    if j-1 >= 0 and input[i][j-1] == nc:
        r = find_trails(i, j-1, nc, r, do_check)
    if j+1 < w and input[i][j+1] == nc:
        r = find_trails(i, j+1, nc, r, do_check)
    return r

print(sum([sum([len(find_trails(i, j, 0, [])) for j in range(w) if input[i][j] == 0]) for i in range(h)]))
print(sum([sum([len(find_trails(i, j, 0, [], False)) for j in range(w) if input[i][j] == 0]) for i in range(h)]))
