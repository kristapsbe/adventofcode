with open("input.txt", "r") as f:
    data = [i.split("-") for i in f.read().strip().split(",")]

p1 = 0
p2 = 0
for e in data:
    min_val = int(e[0])
    max_val = int(e[1])
    min_p1 = e[0][: len(e[0]) // 2]
    max_p1 = e[1][: len(e[1]) // 2 + len(e[1]) % 2]

    for i in range(int(min_p1 if min_p1 else "0"), int(max_p1) + 1):
        tmp = int(f"{i}{i}")
        if tmp > max_val:
            break
        if tmp >= min_val:
            p1 += tmp

    p2_invalids = set()
    for i in range(0, int(max_p1) + 1):
        for j in range(1, len(e[1]) + 1):
            tmp = int(str(i) * (j + 1))
            if tmp > max_val:
                break
            if tmp >= min_val:
                p2_invalids.add(tmp)
    p2 += sum(p2_invalids)
print(p1)
print(p2)
