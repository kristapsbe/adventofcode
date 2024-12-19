lines = [l.strip() for l in open("input.txt", "r").readlines()]
towels = lines[0].split(", ")
designs = lines[2:]

#print(towels)
#print(designs)

def can_design(c, d):
    if c == d:
        return True
    elif len(c) > len(d) or c != d[:len(c)]:
        return False
    else:
        for t in towels:
            if can_design(c+t, d):
                return True
        return False


def memoize(func):
    cache = {}
    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return inner


@memoize
def num_designs(c, d):
    if c == d:
        return 1
    elif len(c) > len(d) or c != d[:len(c)]:
        return 0
    else:
        return sum([num_designs(c+t, d) for t in towels])


ct = 0
nd = 0
for d in designs:
    if can_design("", d):
        ct += 1
    nd += num_designs("", d)

print(ct)
print(nd)
