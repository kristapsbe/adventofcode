from functools import cache

with open("input.txt", "r") as f:
    conns = {l.split(":")[0]: tuple(l.strip().split(" ")[1:]) for l in f.readlines()}


@cache
def solve(pos, target="out"):
    if pos == target:
        return 1
    else:
        if pos == "out":
            return 0
        else:
            return sum([solve(npos, target) for npos in conns[pos]])


p1 = solve("you")
print(p1)

p21 = solve("svr", "dac")
p22 = solve("dac", "fft")
p23 = solve("fft", "out")
p24 = solve("svr", "fft")
p25 = solve("fft", "dac")
p26 = solve("dac", "out")
print((p21 * p22 * p23) + (p24 * p25 * p26))
