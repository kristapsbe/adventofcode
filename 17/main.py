from heapq import heappop, heappush # TODO: still need to do some figuring out - got this from reddit
# https://adventofcode.com/2023/day/17


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/17/input
    lines = [[int(c) for c in l.strip()] for l in f.read().split("\n") if l.strip() != ""]

h = len(lines)
w = len(lines[0])
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)] # direction we're allowed to move in


def get_min_path(min_i, max_i): # TODO: so this does at least work, but I really need to refactor it to figure out why
    q = [(0, 0, 0, -1)]
    seen = set()
    cs = {}

    while len(q) > 0:
        c, i, j, d = heappop(q) # gets whatever is at the top of the queue - TODO: not sure if the rest of the q keeps its order
        if i == h-1 and j == w-1: # TODO: figure out why can we always stop at this point
            return c
        
        if (i, j, d) not in seen: # have we approached these coords from this direction before?
            seen.add((i, j, d)) # now we have
            for nd in range(4): # look in all 4 directions
                ci = 0 # TODO: why are we keeping track of cost on a per-direction basis?
                if nd != d and (nd+2)%4 != d: # TODO: am I reading this right - do we only do direction changes (?)
                    for dist in range(1, max_i+1): # TODO: why are we just running up to the max allowed distance?
                        ni = i+moves[nd][0]*dist # TODO: why multi?
                        nj = j+moves[nd][1]*dist
                        if ni >= 0 and nj >= 0 and ni < h and nj < w: # make sure we're not trying to fall off the board
                            ci += lines[ni][nj]
                            if dist >= min_i: # have we made at least n steps straight
                                nc = c+ci
                                c_id = (ni, nj, nd) # minimum distance for a given (i coord, j coord, direction) 
                                if c_id not in cs or cs[c_id] > nc: # we've either not scored the cell or this is the lowest score we've seen
                                    cs[c_id] = nc
                                    heappush(q, (nc, ni, nj, nd)) # pushes new entry to beginning of q


print(f"PART ONE: {get_min_path(0, 3)}")
print(f"PART TWO: {get_min_path(4, 10)}")