# https://adventofcode.com/2023/day/19


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/test.txt', 'r') as f: # https://adventofcode.com/2023/day/19/input
    lines = [l.strip() for l in f.read().split("\n") if l.strip() != ""]

# PART ONE - try naiive
rules = {}
parts = []
for l in lines:
    if l[0] == "{": # part
        tmp = {}
        for e in l[1:-1].split(","):
            p = e.split("=")
            tmp[p[0]] = int(p[1])
        parts.append(tmp)
    else: # rule
        p1 = l.split("{")
        tmp = []
        for p in p1[1][:-1].split(","):
            p2 = p.split(":")
            if len(p2) > 1:
                if "<" in p2[0]:
                    p3 = p2[0].split("<")
                    tmp.append((p3[0], int(p3[1]), lambda a,b: a<b, p2[-1]))
                else:
                    p3 = p2[0].split(">")
                    tmp.append((p3[0], int(p3[1]), lambda a,b: a>b, p2[-1]))
            else:
                tmp.append(("", "", lambda a,b: True, p2[-1]))

        rules[p1[0]] = tmp

accepted = []
rejected = []
sr = "in"

for p in parts:
    #print(p)
    r = sr
    while r != "A" and r != "R":
        #print(r)
        #print(rules[r])
        for rl in rules[r]:
            if (rl[0] in p and rl[2](p[rl[0]], rl[1])) or rl[0] == '':
                r = rl[3]
                break

    if r == "A":
        accepted.append(p)
    if r == "R":
        rejected.append(p)

#print(accepted)
#print(rejected)

print(sum([sum(a.values()) for a in accepted]))

# PART TWO - whelp - should've gone with this first time round
va = {
    "x": [0, 4000],
    "m": [0, 4000],
    "a": [0, 4000],
    "s": [0, 4000]
}

srules = rules
print(srules)
# step one - simplify - get rid of rules that can only resolve to A or R
while True:
    onlya = [e for e,r in srules.items() if len([rl for rl in r if rl[3] != "A"]) == 0]
    onlyr = [e for e,r in srules.items() if len([rl for rl in r if rl[3] != "R"]) == 0]

    tmp_rules = {}
    for r,rs in srules.items():
        if r in onlya or r in onlyr:
            continue
        tmp_rules[r] = [(rl[0], rl[1], rl[2], "A") if rl[3] in onlya else ((rl[0], rl[1], rl[2], "R") if rl[3] in onlyr else rl) for rl in rs]
    srules = tmp_rules

    if len(onlya) == 0 and len(onlyr) == 0:
        break

print(srules)