def memoize(func):
    cache = {}
    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return inner


dirs = {
    (0, 1): ">", (0, -1): "<", (-1, 0): "^", (1, 0): "v"
}

keypad_pos = {
    "A": (0, 2),
    "^": (0, 1),
    "v": (1, 1),
    "<": (1, 0),
    ">": (1, 2),
}

numpad_pos = {str(i+1): (2-(i//3), i%3) for i in range(9)}
numpad_pos["0"] = (3, 1)
numpad_pos["A"] = (3, 2)

not_allowed = {
    "0": "<",
    "1": "v",
    "4": "vv",
    "7": "vvv",
    "^": "<",
    "<": "^",
    "A": "<<"
}


def make_routes(k, id, jd):
    return [e for e in list(set([
        (("^" if id < 0 else "v")*abs(id))+(("<" if jd < 0 else ">")*abs(jd)),
        (("<" if jd < 0 else ">")*abs(jd))+(("^" if id < 0 else "v")*abs(id))
    ])) if k not in not_allowed or not_allowed[k] != e[:len(not_allowed[k])]]


pads = {
    "k": {k: {ki: make_routes(k, vi[0]-v[0], vi[1]-v[1]) for ki, vi in keypad_pos.items()} for k,v in keypad_pos.items()},
    "n": {k: {ki: make_routes(k, vi[0]-v[0], vi[1]-v[1]) for ki, vi in numpad_pos.items()} for k,v in numpad_pos.items()}
}


@memoize
def expand_path(path, pad):
    pos = "A"
    e_paths = [""]
    for c in path:
        tmp_paths = []
        for p in e_paths:
            for n in pads[pad][pos][c]:
                tmp_paths.append(p+n+"A")
        e_paths = tmp_paths
        pos = c
    return e_paths


@memoize
def get_shortest(path, k, pad):
    expanded = expand_path(path, pad)
    if k < 1:
        return min([len(e) for e in expanded])
    else:
        return min([sum([get_shortest(p+"A", k-1, "k") for p in e.split("A")]) for e in expanded])-1


#print({l.strip(): get_shortest(l.strip(), 2, "n") for l in open("test.txt", "r").readlines()})
print(sum([int(l.strip()[:3])*get_shortest(l.strip(), 2, "n") for l in open("input.txt", "r").readlines()]))
print(sum([int(l.strip()[:3])*get_shortest(l.strip(), 25, "n") for l in open("input.txt", "r").readlines()]))
