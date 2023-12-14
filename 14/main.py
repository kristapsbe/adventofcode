# https://adventofcode.com/2023/day/14


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/14/input
    lines = [l.strip() for l in f.read().split("\n") if l.strip() != ""]


#for l in lines:
#	print(l)

h = len(lines)
w = len(lines[0])


# TODO: geting rid of all of the string ops would probably speed this up massively
def roll_rocks(board, direction):
    area = board.split("\n")
    new_board = [[e if e != "O" else "." for e in b] for b in area]
    new_rocks = []
    if direction == 0: # roll north
        for j in range(w):
            skipped = 0
            for i in range(h):
                if area[i][j] == 'O':
                    new_rocks.append((i-skipped, j))
                elif area[i][j] == '.':
                    skipped = skipped+1
                else:
                    skipped = 0
    elif direction == 1: # roll west
        for i in range(h):
            skipped = 0
            for j in range(w):
                if area[i][j] == 'O':
                    new_rocks.append((i, j-skipped))
                elif area[i][j] == '.':
                    skipped = skipped+1
                else:
                    skipped = 0
    elif direction == 2: # roll south
        for j in range(w):
            skipped = 0
            for i in range(h-1, -1, -1):
                if area[i][j] == 'O':
                    new_rocks.append((i+skipped, j))
                elif area[i][j] == '.':
                    skipped = skipped+1
                else:
                    skipped = 0
    else: # roll east
        for i in range(h):
            skipped = 0
            for j in range(w-1, -1, -1):
                if area[i][j] == 'O':
                    new_rocks.append((i, j+skipped))
                elif area[i][j] == '.':
                    skipped = skipped+1
                else:
                    skipped = 0
    for r in new_rocks:
        new_board[r[0]][r[1]] = "O"
    return "\n".join(["".join(r) for r in new_board])


def score(board):
    ret = []
    for i in range(len(board)):
        for e in board[i]:
            if e == "O":
                ret.append(h-i)
    return sum(ret)

res_one = score(roll_rocks("\n".join(lines), 0).split("\n"))
print(f"PART ONE: {res_one}")

#for l in roll_rocks("\n".join(lines), 0).split("\n"):
#	print(l)

seen_states = []
tot_i = 1000000000*4
board = "\n".join(lines)
for i in range(tot_i):
    if (board, i%4) in seen_states:
        break
    seen_states.append((board, i%4))

    board = roll_rocks(board, i%4)

    #print()
    #for l in board.split("\n"):
    #	print(l)

res_two = 0
if (board, i%4) in seen_states:
    si = seen_states.index((board, i%4)) # how far in the loop were we when we found the repeat
    loop_states = seen_states[si:] # states that result in the loop
    rt = (tot_i-i) # remaining turns
	
    res_two = score(loop_states[rt%len(loop_states)][0].split("\n"))

    #for l in loop_states[rt%len(loop_states)][0].split("\n"):
    #	print(l)
else:
    res_two = score(board.split("\n"))

    #for l in board.split("\n"):
    #	print(l)
print(f"PART TWO: {res_two}")
