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


keypad = {k: {ki: make_routes(k, vi[0]-v[0], vi[1]-v[1]) for ki, vi in keypad_pos.items()} for k,v in keypad_pos.items()}
numpad = {k: {ki: make_routes(k, vi[0]-v[0], vi[1]-v[1]) for ki, vi in numpad_pos.items()} for k,v in numpad_pos.items()}


def generate_paths(seqs, pad):
    output_paths = {}
    for k, v in seqs.items():
        pos = "A"
        paths = []
        for ve in v:
            e_paths = [""]
            for c in ve:
                tmp_paths = []
                for p in e_paths:
                    for n in pad[pos][c]:
                        tmp_paths.append(p+n+"A")
                e_paths = tmp_paths
                pos = c
            paths += e_paths
        output_paths[k] = list(set(paths))
    return output_paths

paths = {l.strip(): [l.strip()] for l in open("input.txt", "r").readlines()}
paths = generate_paths(paths, numpad)
for i in range(2):
    #print(i)
    paths = generate_paths(paths, keypad)

print(sum([int(k[:3])*min([len(e) for e in v]) for k, v in paths.items()]))

paths = {l.strip(): [l.strip()] for l in open("input.txt", "r").readlines()}
paths = generate_paths(paths, numpad)
for i in range(25):
    #print(i)
    paths = generate_paths(paths, keypad)

print(sum([int(k[:3])*min([len(e) for e in v]) for k, v in paths.items()]))
