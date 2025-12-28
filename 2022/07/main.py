with open("input.txt", "r") as f:
    data = [e.strip() for e in f.readlines()]


def populate_d_struct(d_struct, cds, d):
    if len(cds) == 0:
        if d[0] == "dir":
            d_struct[d[1]] = {}
        else:
            d_struct[d[1]] = int(d[0])
    else:
        if cds[0] not in d_struct:
            d_struct[cds[0]] = {}
        d_struct[cds[0]] = populate_d_struct(d_struct[cds[0]], cds[1:], d)
    return d_struct


d_struct = {}
cds = []
for d in data:
    if d[0] == "$":
        tmp = d.split()
        if tmp[1] == "cd":
            match tmp[2]:
                case "/":
                    cds = []
                case "..":
                    cds = cds[:-1]
                case _:
                    cds.append(tmp[2])
    else:
        d_struct = populate_d_struct(d_struct, cds, d.split())


def calc_dir_sizes(d_struct):
    tot_size = 0
    children = {}
    for k, v in d_struct.items():
        if isinstance(v, int):
            tot_size += v
        else:
            children[k] = calc_dir_sizes(d_struct[k])
            tot_size += children[k][0]
    return (tot_size, children)


dir_sizes = calc_dir_sizes(d_struct)


def flatten_dict(dir_sizes, dir_name):
    tmp = {dir_name: dir_sizes[0]}
    for k, v in dir_sizes[1].items():
        tmp |= flatten_dict(v, f"{dir_name}_{k}")
    return tmp


flat_dir_sizes = flatten_dict(dir_sizes, "/")

print(sum([v for v in flat_dir_sizes.values() if v <= 100000]))

total_space = 70000000
min_unused = 30000000
curr_used = flat_dir_sizes["/"]
min_delete = min_unused - (total_space - curr_used)

print(min([v for v in flat_dir_sizes.values() if v >= min_delete]))
