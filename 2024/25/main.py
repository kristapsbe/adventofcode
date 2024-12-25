keys = []
locks = []

with open("input.txt", "r") as f:
    is_key = False
    is_lock = False
    tmp = [0, 0, 0, 0, 0]
    for l in f.readlines():
        ls = l.strip()
        if ls == "":
            if is_key:
                keys.append([e-1 for e in tmp])
            if is_lock:
                locks.append(tmp)
            is_key = False
            is_lock = False
            tmp = [0, 0, 0, 0, 0]
            continue

        if not is_key and not is_lock:
            is_key = (ls != "#####")
            is_lock = not is_key
        else:
            for i in range(5):
                if ls[i] == "#":
                    tmp[i] += 1

    if is_key:
        keys.append([e-1 for e in tmp])
    if is_lock:
        locks.append(tmp)

r = 0
for l in locks:
    for k in keys:
        match = True
        for i in range(5):
            if l[i]+k[i] > 5:
                match = False
                break
        if match:
            r += 1
print(r)
