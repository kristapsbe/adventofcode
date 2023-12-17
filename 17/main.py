# https://adventofcode.com/2023/day/17


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/test.txt', 'r') as f: # https://adventofcode.com/2023/day/17/input
    lines = [[int(c) for c in l.strip()] for l in f.read().split("\n") if l.strip() != ""]

h = len(lines)
w = len(lines[0])

# PART ONE
min_p = h*w*999
max_s = 3 # max number of cells we're allowed to move straight
# starting to the right and to the bottom 
# (current i, current j, how moving straight, turn counter, current heat)
ns = [(0, 0, 0, 1, 0), (0, 0, 0, 2, 0)] 
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
move_l = len(moves)-1

while len(ns) > 0: # keep going while we have paths to explore
    # try to enter nodes we had planned to enter
    tmp_ns = []
    for n in ns:
        ni = n[0]+moves[n[3]][0]
        nj = n[1]+moves[n[3]][1]
        #print(f"{ni} {nj} {h} {w}")
        if ni >= 0 and nj >= 0 and ni < h and nj < w: 
            #print(f"{ni} {nj}")
            np = n[4]+lines[ni][nj]
            if np < min_p:
                if ni == (h-1) and nj == (w-1):
                    min_p = np
                else:
                    # note - even if we turned to get here we're always technically making a move straight ahead
                    tmp_ns.append((ni, nj, n[2]+1, n[3], np))
    # figure out what potential directions could we go from the nodes that we've entered
    next_ns = []
    for n in tmp_ns:
        if n[2] < max_s: # not exceeded straight move allowance - let it keep going
            next_ns.append(n)
        if n[3] > 1: # no loop to the right - add route to the right
            next_ns.append((n[0], n[1], 0, n[3]-1, n[4]))
        if n[3] < move_l: # no loop to the left - add route to the left
            next_ns.append((n[0], n[1], 0, n[3]+1, n[4]))
    #print()
    #print(ns)
    #print(tmp_ns)
    #print(next_ns)
    ns = next_ns

print(min_p)