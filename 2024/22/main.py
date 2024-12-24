# https://www.reddit.com/r/adventofcode/comments/1hl4gqe/2024_day_22_part_1_2000_iterations_in_less_than_1/
# this is probably worth taking a look at
inputs = [int(l) for l in open("input.txt", "r").readlines()]

seqs = {}


def get_nth_numer(seed, id, n):
    res = seed
    s1 = -1
    s2 = -1
    s3 = -1
    s4 = -1
    c = seed%10
    d = 0
    for i in range(n):
        res = ((res*64)^res)%16777216
        res = ((res//32)^res)%16777216
        res = ((res*2048)^res)%16777216

        d = (res%10)-c
        c += d
        s1 = s2
        s2 = s3
        s3 = s4
        s4 = d

        if i > 4:
            seq = (s1, s2, s3, s4)
            if seq not in seqs:
                seqs[seq] = {
                    id: c
                }
            elif id not in seqs[seq]:
                seqs[seq][id] = c
    return res


print(sum([get_nth_numer(inputs[i], i, 2000) for i in range(len(inputs))]))
bananas = {k: sum(v.values()) for k, v in seqs.items()}
print(bananas[max(bananas, key=bananas.get)])
