import math

with open("input.txt", "r") as f:
    data = [[c for c in e.strip().split()] for e in f.readlines()]

nums = [[int(c) for c in r] for r in data[:-1]]
opers = data[-1]
probs = len(opers)
n_len = len(nums)

p1 = 0
for p in range(probs):
    match opers[p]:
        case "+":
            p1 += sum([numr[p] for numr in nums])
        case "*":
            p1 += math.prod([numr[p] for numr in nums])
print(p1)

with open("input.txt", "r") as f:
    lines = f.readlines()
    max_l = max([len(l) for l in lines])
    only_spaces = set([i for i, c in enumerate(lines[0]) if c == " "])
    for l in lines[1:]:
        only_spaces &= set([i for i, c in enumerate(l) if c == " "])
    nums = []
    curr_nums = []
    i = 0
    j = 0
    for i in range(max_l):
        if i in only_spaces:
            nums.append([int(c.strip()) for c in curr_nums if c.strip()])
            curr_nums = []
        else:
            curr_nums.append(
                "".join(
                    [lines[j][i] if i < len(lines[j]) else "" for j in range(n_len)]
                )
            )
    nums.append([int(c.strip()) for c in curr_nums if c.strip()])

p2 = 0
for p in range(probs):
    match opers[p]:
        case "+":
            p2 += sum([numr for numr in nums[p]])
        case "*":
            p2 += math.prod([numr for numr in nums[p]])
print(p2)
