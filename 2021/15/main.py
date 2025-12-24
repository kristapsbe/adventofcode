# p2 broken atm use prio q and a•
from math import inf

with open("input.txt", "r", encoding="utf-8") as f:
    data = [[int(c) for c in l.strip()] for l in f.readlines()]

dists = [[inf for _ in range(len(data[0]))] for _ in range(len(data))]


def calc_min_dist_to_start(i, j, d):
    if i == 0 and j == 0:
        return d

    res = [inf]
    if i > 0:
        new_d = d + data[i - 1][j]
        if dists[i - 1][j] > new_d:
            dists[i - 1][j] = new_d
            res.append(calc_min_dist_to_start(i - 1, j, new_d))
    if j > 0:
        new_d = d + data[i][j - 1]
        if dists[i][j - 1] > new_d:
            dists[i][j - 1] = new_d
            res.append(calc_min_dist_to_start(i, j - 1, new_d))
    return min(res)


print(calc_min_dist_to_start(len(data) - 1, len(data[0]) - 1, 0))
# print(dists)

big_data_tmp = [[[((c - 1 + i) % 9 + 1) for c in d] for d in data] for i in range(10)]

ct = len(data[0])
data = []
for tr in range(5):
    for r in range(ct):
        tmpr = []
        for bd in big_data_tmp[0 + tr : 5 + tr]:
            tmpr += bd[r]
        data.append(tmpr)

dists = [[inf for _ in range(len(data[0]))] for _ in range(len(data))]

print(calc_min_dist_to_start(len(data) - 1, len(data[0]) - 1, 0))

# for l in dists:
#     print(l)
