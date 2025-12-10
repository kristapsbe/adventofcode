from functools import cache

with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

# indicators = [[c == "#" for c in e.split("]")[0][1:]] for e in data]
indicators = [e.split("]")[0][1:] for e in data]
num_lights = len(indicators)
buttons = [
    [set([int(c) for c in p[1:-1].split(",")]) for p in e.split(" ")[1:-1]]
    for e in data
]
joltage = [tuple(int(c) for c in e.split("{")[1][:-1].split(",")) for e in data]

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

p2 = 0
for i in range(num_lights):
    seen = set([tuple(0 for _ in joltage[i])])
    curr_joltages = [tuple(0 for _ in joltage[i])]
    ct = 0
    while joltage[i] not in seen and len(curr_joltages) > 0:
        # print(seen, curr_lights)
        new_joltages = []
        for cj in curr_joltages:
            for b in buttons[i]:
                tmp_c = tuple([j + 1 if ci in b else j for ci, j in enumerate(cj)])
                # print(cl, tmp_c, b)
                if tmp_c not in seen and all(
                    [j <= joltage[i][ci] for ci, j in enumerate(cj)]
                ):
                    seen.add(tmp_c)
                    new_joltages.append(tmp_c)
        # print(curr_joltages, new_joltages, seen)
        curr_joltages = new_joltages
        ct += 1
    print(ct, i, num_lights)
    p2 += ct
print(p2)
