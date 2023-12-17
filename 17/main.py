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
        cost, i, j, d = heappop(q)
        if i == h-1 and j == w-1: # TODO: figure out why can we always stop at this point
            return cost
        
        if (i, j, d) not in seen:
            seen.add((i, j, d))
            for direction in range(4):
                costincrease = 0
                if direction != d and (direction + 2) % 4 != d: # can't go this way
                    for distance in range(1, max_i + 1):
                        ni = i+moves[direction][0]*distance
                        nj = j+moves[direction][1]*distance
                        if ni in range(len(lines)) and nj in range(len(lines[0])):
                            costincrease += lines[ni][nj]
                            if distance >= min_i:
                                nc = cost + costincrease
                                if cs.get((ni, nj, direction), 1e100) > nc:
                                    cs[(ni, nj, direction)] = nc
                                    heappush(q, (nc, ni, nj, direction))


print(f"PART ONE: {get_min_path(0, 3)}")
print(f"PART TWO: {get_min_path(4, 10)}")