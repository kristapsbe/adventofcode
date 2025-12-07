from functools import cache

with open("input.txt", "r") as f:
    lines = f.readlines()

started = False
p1 = 0
# todo: there has to be a way to do this w-out recursion
# p2 = 1
beams = set()
for l in lines:
    if not started:
        s = set(i for i, c in enumerate(l) if c == "S")
        if len(s) > 0:
            beams |= s
            started = True
    else:
        splitters = set(i for i, c in enumerate(l) if c == "^")
        hit_slitters = splitters & beams
        p1 += len(hit_slitters)
        # if len(hit_slitters) > 0:
        # p2 *= len(hit_slitters)
        new_beams = set()
        for hs in hit_slitters:
            new_beams.add(hs - 1)
            new_beams.add(hs + 1)
        beams -= hit_slitters
        beams |= new_beams
print(p1)
# print(p2)

splitters = [set(i for i, c in enumerate(l) if c == "^") for l in lines if "^" in l]


@cache
def calc_p2(p, d, ds):
    if d >= ds:
        return 1
    else:
        if p in splitters[d]:
            return calc_p2(p - 1, d + 1, ds) + calc_p2(p + 1, d + 1, ds)
        else:
            return calc_p2(p, d + 1, ds)


print(calc_p2(lines[0].index("S"), 0, len(splitters)))
