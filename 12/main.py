from functools import cache
# https://adventofcode.com/2023/day/12


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/12/input
    lines = [l.strip() for l in f.read().split("\n") if l.strip() != ""]

conds = [l.split(" ")[0] for l in lines]
groups = [[int(c) for c in l.split(" ")[1].split(",")] for l in lines]


# copied speedier implementation from https://github.com/ypisetsky/advent-of-code-2023/blob/main/day12.py
# note to self - brush up on dynamic programming
# TODO: take a look at https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2F2023-day-12-part-2-this-image-helped-a-few-people-to-solve-v0-46y3l042m06c1.png%3Fs%3Dd944fffd4f3b4f73ac26c336af377d35bd364e9f
# looks like a cool way to go about it
@cache
def count_valid_states(line, counts, pos, current_count, countpos):
      # pos is the next character to be processed
      # current_count is how far into the current sequence of #s we are in
      # countpos is how many sequences of #s we have already finished
      if pos == len(line):
            ret = 1 if len(counts) == countpos else 0
      elif line[pos] == '#':
            ret = count_valid_states(line, counts, pos + 1, current_count + 1, countpos)
      elif line[pos] == '.' or countpos == len(counts):
            if countpos < len(counts) and current_count == counts[countpos]:
                  ret = count_valid_states(line, counts, pos + 1, 0, countpos + 1)
            elif current_count == 0:
                  ret = count_valid_states(line, counts, pos + 1, 0, countpos)
            else:
                  ret = 0
      else:
            hash_count = count_valid_states(line, counts, pos + 1, current_count + 1, countpos)
            dot_count = 0
            if current_count == counts[countpos]:
                  dot_count = count_valid_states(line, counts, pos + 1, 0, countpos + 1)
            elif current_count == 0:
                  dot_count = count_valid_states(line, counts, pos + 1, 0, countpos)
            ret = hash_count + dot_count
      return ret


# PART ONE
res = []
for i in range(len(conds)):
    res.append(count_valid_states(conds[i] + '.', tuple(groups[i]), 0, 0, 0))

#print(res)
print(f"PART ONE: {sum(res)}")

# PART TWO
scale_f = 5
res = []
for i in range(len(conds)):
    s_group = groups[i]*scale_f
    s_conds = "?".join([conds[i] for _ in range(scale_f)])
    res.append(count_valid_states(s_conds+'.', tuple(s_group), 0, 0, 0))

#print(res)
print(f"PART TWO: {sum(res)}")
