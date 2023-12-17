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
# (current i, current j, direction i, direction j, how moving straight, turn counter, current heat)
ns = [(0, 0, 0, 1, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0)] 

while len(ns) > 0: # keep going while we have paths to explore
    tmp_ns = []
    # first - try to enter nodes we had planned to enter
    for n in ns:
        ni = n[0]+n[2]
        nj = n[1]+n[3]
        nstr = n[4]+1
        
    ns = tmp_ns