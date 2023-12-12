import math
# https://adventofcode.com/2023/day/12


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/12/input
    lines = [l.strip() for l in f.read().split("\n") if l.strip() != ""]

# PART ONE
conds = [l.split(" ")[0] for l in lines]
groups = [[int(c) for c in l.split(" ")[1].split(",")] for l in lines]


def find_valid_states(curr_s, group, conds, c_len, b=1):
    if len(group) == 0:
        min_common = min(len(curr_s), c_len)
        if len([i for i in range(min_common) if curr_s[i] != conds[i] and conds[i] != '?']) == 0 and len([c for c in conds[min_common:] if c == '#']) == 0 and len([c for c in curr_s[min_common:] if c == '#']) == 0:
            #print(f"VALID {curr_s} ({conds})")
            return 1
        else:
            #print(f"INVALID {curr_s} ({conds})")
            #print([i for i in range(min_common) if curr_s[i] != conds[i] and conds[i] != '?'])
            #print([c for c in conds[min_common:] if c == '#'])
            #print([c for c in curr_s[min_common:] if c == '#'])
            return 0
    else:
        min_l = len(f"{curr_s}.{group[0]}")
        if min_l > c_len:
            #print(f"TOO LONG {curr_s} ({conds})")
            return 0
        else:
            rets = []
            for i in range(c_len-min_l+1):
                rets.append(find_valid_states(f'{curr_s}{"."*(i+b)}{"#"*group[0]}', group[1:], conds, c_len))
            return sum(rets)


res = []
for i in range(len(conds)):
    res.append(find_valid_states("", groups[i], conds[i], len(conds[i]), 0))

#print(res)
print(sum(res))