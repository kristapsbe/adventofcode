import math
# https://adventofcode.com/2023/day/12


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/12/input
    lines = [l.strip() for l in f.read().split("\n") if l.strip() != ""]

conds = [l.split(" ")[0] for l in lines]
groups = [[int(c) for c in l.split(" ")[1].split(",")] for l in lines]


# TODO: this is horribly slow - I tried to look for a bit of inspiration and I guess the solution is to go character by character
# and to cache whatever the state at a given character was - e.g. - https://github.com/ypisetsky/advent-of-code-2023/blob/main/day12.py
# note to self - brush up on dynamic programming
def find_valid_states(curr_s, group, new_group_cap, conds, c_len, min_common, min_space=1):
    if len([i for i in range(min_common) if curr_s[i] != conds[i] and conds[i] != '?']) == 0:
        if len(group) == 0:
            if len([c for c in conds[min_common:] if c == '#']) == 0 and len([c for c in curr_s[min_common:] if c == '#']) == 0:
                return 1
            else:
                return 0
        else:
            min_l = len(f".{group[0]}")
            if min_l > c_len:
                return 0
            else:
                rets = []
                for i in range(c_len-min_l-new_group_cap):
                    new_s = f'{"."*(i+min_space)}{"#"*group[0]}'
                    new_group_cap = sum(group[2:])+len(group)-3
                    new_conds = conds[len(curr_s):]
                    new_c_len = len(new_conds)
                    rets.append(find_valid_states(new_s, group[1:], new_group_cap, new_conds, new_c_len, min(len(new_s), new_c_len)))
                return sum(rets)
    else:
        return 0


# PART ONE
res = []
for i in range(len(conds)):
    res.append(find_valid_states("", groups[i], sum(groups[i][1:])+len(groups[i])-3, conds[i], len(conds[i]), 0, 0))

#print(res)
print(f"PART ONE: {sum(res)}")

# PART TWO
scale_f = 5
res = []
for i in range(len(conds)):
    s_group = groups[i]*scale_f
    s_conds = "?".join([conds[i] for _ in range(scale_f)])
    res.append(find_valid_states("", s_group, sum(s_group[1:])+len(s_group)-3, s_conds, len(s_conds), 0, 0))

#print(res)
print(f"PART TWO: {sum(res)}")
