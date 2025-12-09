import numpy as np

with open("input.txt", "r") as f:
    data = [[int(c) for c in l.strip().split(",")] for l in f.readlines()]

num_coords = len(data)

min_x = 100_000
max_x = 0
min_y = 100_00
max_y = 0

p1 = 0
for i in range(num_coords):
    min_x = min(data[i][0], min_x)
    max_x = max(data[i][0], max_x)
    min_y = min(data[i][1], min_y)
    max_y = max(data[i][1], max_y)
    for j in range(i + 1, num_coords):
        curr_rect = (abs(data[i][0] - data[j][0]) + 1) * (
            abs(data[i][1] - data[j][1]) + 1
        )
        p1 = max(curr_rect, p1)
print(p1)

green = np.zeros((max_x - min_x + 1, max_y - min_y + 1))
for i in range(-1, num_coords - 1):
    cxs = sorted([data[i][0] - min_x, data[i + 1][0] - min_x])
    cys = sorted([data[i][1] - min_y, data[i + 1][1] - min_y])
    green[cxs[0] : cxs[1] + 1, cys[0] : cys[1] + 1] = 1


p2 = 0
for i in range(-2, num_coords - 2):
    # print(data[i], data[i + 1], data[i + 2])
    fourth = [0, 0]
    for j in range(2):
        coords = [data[i + k][j] for k in range(3)]
        if coords[0] == coords[1]:
            fourth[j] = coords[2]
        elif coords[0] == coords[2]:
            fourth[j] = coords[1]
        else:
            fourth[j] = coords[0]
    others = [
        [data[i + k][0] - min_x, data[i + k][1] - min_y]
        for k in range(3)
        if bool(data[i + k][0] != fourth[0]) != bool(data[i + k][1] != fourth[1])
    ]
    fourth[0] -= min_x
    fourth[1] -= min_y
    # if green[fourth[0], fourth[1]]:
    #     curr_rect = (abs(data[i][0] - data[i + 2][0]) + 1) * (
    #         abs(data[i][1] - data[i + 2][1]) + 1
    #     )
    #     p2 = max(curr_rect, p2)
    # else:
    # dirs = [
    #     green[fourth[0], : fourth[1]],
    #     green[fourth[0], fourth[1] :],
    #     green[fourth[0] :, fourth[1]],
    #     green[: fourth[0], fourth[1]],
    # ]
    dirs = [
        green[
            min(o[0], fourth[0]) : max(o[0], fourth[0]) + 1,
            min(o[1], fourth[1]) : max(o[1], fourth[1]) + 1,
        ][0]
        for o in others
    ]
    # print(others, fourth, dirs, [data[i + k] for k in range(3)])
    is_one = True
    for j, d in enumerate(dirs):
        # print(d)
        starts = (d == 1) & np.concatenate(([True], d[:-1] == 0))
        count = np.sum(starts)
        if count > 1:
            is_one = False
            break
    if is_one:
        curr_rect = (abs(data[i][0] - data[i + 2][0]) + 1) * (
            abs(data[i][1] - data[i + 2][1]) + 1
        )
        # if curr_rect >= p2:
        # print(data[i], data[i + 2], curr_rect, fourth, min_x, min_y)
        p2 = max(curr_rect, p2)
    # print(
    #     fourth,
    #     green[fourth[0], fourth[1]],
    #     green[fourth[0], : fourth[1]],
    #     green[fourth[0], fourth[1] :],
    #     green[fourth[0] :, fourth[1]],
    #     green[: fourth[0], fourth[1]],
    # )
    # starts = (a == 1) & np.concatenate(([True], a[:-1] == 0))
    # count = np.sum(starts)
    # get fourth corner - if the fourth corner passes an odd number of ones
    # to hit either of the 0 edges = inside
# print(p1)
# broken - ans = 1544362560 -> fix (it's a circle with an inset thing (with the shape being right below an inset in the middle))
print(p2)

# print(green)
