# https://adventofcode.com/2023/day/17


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/test.txt', 'r') as f: # https://adventofcode.com/2023/day/17/input
    lines = [[int(c) for c in l.strip()] for l in f.read().split("\n") if l.strip() != ""]

h = len(lines)
w = len(lines[0])

# PART ONE
min_p = 999999
max_s = 3 # max number of cells we're allowed to move straight
# starting to the right and to the bottom 
# (current i, current j, how long moving straight, direction id, current heat)
ns = [(0, 0, 0, 1, 0), (0, 0, 0, 2, 0)] 
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
visited = [[{} for _ in range(w)] for _ in range(h)]

while len(ns) > 0: # keep going while we have paths to explore
    tmp_ns = []
    for n in ns: # figure out which cells we can move into
        ni = n[0]+moves[n[3]][0]
        nj = n[1]+moves[n[3]][1]
        if ni >= 0 and nj >= 0 and ni < h and nj < w: # check if we're not trying to fall off the board
            np = n[4]+lines[ni][nj] # the heat that we're getting
            p_id = (n[2], n[3])
            if p_id not in visited[ni][nj] or np < visited[ni][nj][p_id]:
                visited[ni][nj][p_id] = np
                if ni != (h-1) or nj != (w-1):
                    # note - even if we turned to get here we're always technically making a move straight ahead
                    tmp_ns.append((ni, nj, n[2]+1, n[3], np))

    # figure out what potential directions could we go from the nodes that we've entered
    next_ns = []
    for n in tmp_ns:
        if n[2] < max_s: # not exceeded straight move allowance - let it keep going
            next_ns.append(n)
        if n[3] > 1: # no loop to the right - add route to the right
            next_ns.append((n[0], n[1], 0, n[3]-1, n[4]))
        if n[3] < len(moves)-1: # no loop to the left - add route to the left
            next_ns.append((n[0], n[1], 0, n[3]+1, n[4]))
    ns = next_ns

for v in visited:
    print(v)
