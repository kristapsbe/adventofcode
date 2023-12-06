import math
# https://adventofcode.com/2023/day/6

lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/6/input
    lines = [[int(c) for c in l.split()[1:]] for l in f.read().split("\n")]

# PART ONE
def get_num_solutions(time, dist): # got this from Einar https://github.com/EinPy
	tmin = math.ceil((time - math.sqrt(time**2 - 4 * dist)) / 2)
	tmax = math.ceil((time + math.sqrt(time**2 - 4 * dist)) / 2)
	return tmax-tmin


res = []
for i in range(len(lines[0])):
	res.append(get_num_solutions(lines[0][i], lines[1][i]))

print(f"PART ONE: {math.prod(res)}")

# PART TWO
# really slow really brute-y - do binary search to find borders?
time = int("".join([str(c) for c in lines[0]]))
dist = int("".join([str(c) for c in lines[1]]))

print(f"PART TWO: {get_num_solutions(time, dist)}")
