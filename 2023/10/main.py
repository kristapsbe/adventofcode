# https://adventofcode.com/2023/day/10


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/10/input
    lines = f.read().split("\n")

# PART ONE
# TODO: https://www.reddit.com/r/adventofcode/comments/18ex3zv/2023_day_10_part_1_spoiler_how_do_i_describe_a/ suggests
# that there's a mathemathical solution - would be cool to take a look
pipes = {
    # note - pretending that this is what the coords looks around the current node c
    # (0,0) (0,1) (0,2)
    # (1,0)   c   (1,2)
    # (2,0) (2,1) (2,2)
    # to make it a bit shorter lower down in the code
    "|": [(0, 1), (2, 1)], # | is a vertical pipe connecting north and south.
    "-": [(1, 0), (1, 2)], # - is a horizontal pipe connecting east and west.
    "L": [(1, 0), (2, 1)], # L is a 90-degree bend connecting north and east.
    "J": [(1, 2), (2, 1)], # J is a 90-degree bend connecting north and west.
    "7": [(0, 1), (1, 2)], # 7 is a 90-degree bend connecting south and west.
    "F": [(0, 1), (1, 0)] # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
}

valid_dirs = { # I forgot that the current pipe can't actually connect to another pipe in any direction
    # note - pretending that this is what the coords looks around the current node c
    # (0,0) (0,1) (0,2)
    # (1,0)   c   (1,2)
    # (2,0) (2,1) (2,2)
    # to make it a bit shorter lower down in the code
    "|": [(0, 1), (2, 1)], # | is a vertical pipe connecting north and south.
    "-": [(1, 0), (1, 2)], # - is a horizontal pipe connecting east and west.
    "L": [(0, 1), (1, 2)], # L is a 90-degree bend connecting north and east.
    "J": [(0, 1), (1, 0)], # J is a 90-degree bend connecting north and west.
    "7": [(1, 0), (2, 1)], # 7 is a 90-degree bend connecting south and west.
    "F": [(1, 2), (2, 1)], # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # I assume S just becomes whatever would fit
    "S": [(0, 1), (2, 1), (1, 0), (1, 2)]# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
}

S = (0, 0) # figure out where we're starting
for si in range(len(lines)):
    if "S" in lines[si]:
        S = (si, lines[si].index("S"))

h = len(lines)
w = len(lines[0])

curr_n = [S] # chunks of pipe we're looking at
conns = {} # chunks of pipe we've looked at (including info on what they connect for (if anything))
while len(curr_n) > 0: # figuring out what connects to what
    next_n = []
    for n in curr_n:
        n_pipe = lines[n[0]][n[1]]
        if n not in conns:
            for i in range(3): # look around the adjacent cells
                for j in range(3):
                    if (i, j) in valid_dirs[n_pipe]:
                        new_n = (n[0]+i-1, n[1]+j-1) # get new coords
                        if new_n[0] >= 0 and new_n[1] >= 0 and new_n[0] < h and new_n[1] < w: # check if we're still inside of the grid
                            tmp_c = lines[new_n[0]][new_n[1]]
                            if tmp_c in pipes and (i, j) in pipes[tmp_c]: # is this a valid pipe at a valid position (i.e. do we connect to something)
                                if n not in conns:
                                    conns[n] = []
                                conns[n].append(new_n)
                                next_n.append(new_n)
    curr_n = next_n

#print(S)
#print(conns)

# prune off pipes that didn't end up connecting to anything
do_delete = True
while do_delete:
    do_delete = False
    for k,v in conns.items():
        tmp = [e for e in v if e in conns]
        if len(tmp) != len(v):
            do_delete = True
        conns[k] = tmp
    tmp_c = {ek:ev for ek,ev in conns.items() if len(v) > 1}
    if len(tmp_c) != len(conns):
        do_delete = True
    conns = tmp_c

#for i in range(h):
#    print("".join([lines[i][j] if (i, j) in conns else " " for j in range(w)]))

print(f"PART ONE: {len(conns)//2}")

# PART TWO
s_offsets = [(c[0]-S[0]+1, c[1]-S[1]+1) for c in conns[S]]
s_char = [k for k,v in valid_dirs.items() if len([so for so in s_offsets if so not in v]) == 0 and k != "S"][0] # I expect to get only one match

io_d = {"F": "J", "L": "7"} # only flips if this is the next vertical pipe char we get 
#     O  I
io = [[], []] 
for i in range(h):
    ct = 0
    wting = ""
    for j in range(w):
        if (i, j) not in conns: # not a part of the pipe, so either an "in" or "out" node
            io[ct%2].append((i, j))
        else: # part of the pipe
            c_line = lines[i][j] if lines[i][j] != "S" else s_char # turning S into the char that it's hiding
            if c_line in io_d: # starting a horizontal bit
                wting = io_d[c_line]
            else:
                if (i, j+1) not in conns[(i, j)]:
                    if (wting == "" or c_line == wting): # figuring out if what we saw was a u-bend or not
                        ct = ct+1
                    wting = ""

#for i in range(h):
#    print("".join(["o" if (i, j) in io[0] else ("i" if (i, j) in io[1] else lines[i][j]) for j in range(w)]))

print(f"PART TWO: {len(io[1])}")