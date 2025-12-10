from copy import copy

with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

# indicators = [[c == "#" for c in e.split("]")[0][1:]] for e in data]
indicators = [e.split("]")[0][1:] for e in data]
num_lights = len(indicators)
buttons = [
    [set([int(c) for c in p[1:-1].split(",")]) for p in e.split(" ")[1:-1]]
    for e in data
]
joltage = [[int(c) for c in e.split("{")[1][:-1].split(",")] for e in data]

l_state = {
    ".": "#",
    "#": ".",
}

p1 = 0
for i in range(num_lights):
    seen = set(["." * len(indicators[i])])
    curr_lights = ["." * len(indicators[i])]
    ct = 0
    while indicators[i] not in seen and len(curr_lights) > 0:
        # print(seen, curr_lights)
        new_lights = []
        for cl in curr_lights:
            for b in buttons[i]:
                tmp_c = "".join([l_state[l] if i in b else l for i, l in enumerate(cl)])
                # print(cl, tmp_c, b)
                if tmp_c not in seen:
                    seen.add(tmp_c)
                    new_lights.append(tmp_c)
        curr_lights = new_lights
        ct += 1
    p1 += ct
print(p1)

# unusably slow - I probably need to work from the constraints that the buttons impose
# check if there's buttons that must be pressed and then go from there
#
# TODO: supposed to be an ILP thing (supposedly z3 can solve this)
# I should work out the math - should be doable with some matrix ops
# solution - 15688
p2 = 0
for i in range(num_lights):
    # getting buttons that are the only ones that affect a given light
    curr_joltage = copy(joltage[i])
    os = tuple(0 for _ in joltage[i])
    skip_buttons = set()
    ct = 0
    while True:
        a_cts = [0 for _ in joltage[i]]
        new_skip_buttons = set()
        zero_cols = set(j for j, _ in enumerate(a_cts) if curr_joltage[j] == 0)
        for bi, b in enumerate(buttons[i]):
            if bi not in skip_buttons:
                for bn in b:
                    if bn in zero_cols:
                        new_skip_buttons.add(bi)
                    else:
                        a_cts[bn] += 1
        for j, a_ct in enumerate(a_cts):
            if a_ct == 1:
                for bi, b in enumerate(buttons[i]):
                    if bi not in skip_buttons and j in b:
                        new_skip_buttons.add(bi)
                        reduction = curr_joltage[j]
                        for bjs in b:
                            curr_joltage[bjs] -= reduction
                        ct += reduction
                        break
        if skip_buttons != (new_skip_buttons | skip_buttons):
            skip_buttons |= new_skip_buttons
            continue
        break

    seen = set([tuple(curr_joltage)])
    curr_joltages = [tuple(curr_joltage)]
    while os not in seen and len(curr_joltages) > 0:
        # print(seen, curr_lights)
        new_joltages = []
        for cj in curr_joltages:
            for bi, b in enumerate(buttons[i]):
                if bi not in skip_buttons:
                    tmp_c = tuple([j - 1 if ci in b else j for ci, j in enumerate(cj)])
                    # print(cl, tmp_c, b)
                    if tmp_c not in seen and min(tmp_c) >= 0:
                        seen.add(tmp_c)
                        new_joltages.append(tmp_c)
        # print(curr_joltages, new_joltages, seen)
        curr_joltages = new_joltages
        ct += 1
    print(ct, i, num_lights)
    p2 += ct
print(p2)
