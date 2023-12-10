# https://adventofcode.com/2023/day/2
import math


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/2/input
    lines = f.read().split("\n")

# PART ONE
max_cubes = {"red": 12, "green": 13, "blue": 14}
# this doesn't really do anything (as the games appear to be ordered (I could just use line number))
game_lines = {int(gl[0].strip().split(" ")[1]): gl[1] for gl in [l.split(":") for l in lines]}
#                                              split number from col             split out each col        split out each draw
parsed_lines = {k: [{e[1]: int(e[0]) for e in [csl.strip().split(" ") for csl in sl.split(",")]} for sl in l.split(";")] for k,l in game_lines.items()}

res = []
for k,v in parsed_lines.items():
    # looking to see if any rows break the rules instead of checking if all pass
    if len([e for e in v if len([ck for ck, cv in e.items() if cv > max_cubes[ck]]) > 0]) == 0:
        res.append(k)

print(f"PART ONE: {sum(res)}")

# PART TWO
min_playable = []
for v in parsed_lines.values():
    min_cubes = {ck: 0 for ck in max_cubes.keys()} # pre-seeding minimun number of cubes we need with 0s
    for game in v:
        for col, cval in game.items(): # use w-e colors have been drawn (means we don't have to check if a colors been drawn)
            min_cubes[col] = max(min_cubes[col], cval) # take the biggest of the values for the color
    min_playable.append(math.prod(min_cubes.values())) # red*green*blue

print(f"PART TWO: {sum(min_playable)}")
