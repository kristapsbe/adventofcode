from functools import cache

with open("input.txt", "r") as f:
    conns = {l.split(":")[0]: tuple(l.strip().split(" ")[1:]) for l in f.readlines()}


@cache
def solve_p1(pos, path, target="out"):
    if pos in path:
        # print("loop", path)
        return 0
    else:
        if pos == target:
            # print("out", path)
            return 1
        else:
            if pos in conns:
                return sum(
                    solve_p1(p, tuple(list(path) + [pos]), target) for p in conns[pos]
                )
            else:
                return 0


# p1 = solve_p1("you", tuple())
# print(p1)


# very slow - could probs use NX or try to split the problem into path srv -> dac + dac -> fft + fft -> out
@cache
def solve_p2(pos, path):
    if pos in path:
        # print("loop", path)
        return 0
    else:
        if pos == "out":
            # print("out", path, int("dac" in path and "fft" in path))
            return int("dac" in path and "fft" in path)
        else:
            return sum(solve_p2(p, tuple(list(path) + [pos])) for p in conns[pos])


# p2 = solve_p2("svr", tuple())
# print(p2)

p21 = solve_p1("svr", tuple(), "dac")
print(p21)
p22 = solve_p1("dac", tuple(), "fft")
print(p22)
p23 = solve_p1("fft", tuple(), "out")
print(p23)
p24 = solve_p1("svr", tuple(), "fft")
print(p24)
p25 = solve_p1("fft", tuple(), "dac")
print(p25)
p26 = solve_p1("dac", tuple(), "out")
print(p26)
print((p21 * p22 * p23) + (p24 * p25 * p26))
