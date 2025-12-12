import sys
from functools import cache

sys.setrecursionlimit(10000)

shape_init = {}
areas = []

with open("input.txt", "r") as f:
    curr_shape = 0
    for l in f:
        tmp = l.strip()
        if tmp:
            if tmp[-1] == ":":
                curr_shape = int(tmp[:-1])
                shape_init[curr_shape] = []
            else:
                if ":" in tmp:
                    parts = tmp.split(": ")
                    areas.append(
                        [
                            [int(p) for p in parts[0].split("x")],
                            [int(p) for p in parts[1].split(" ")],
                        ]
                    )
                else:
                    shape_init[curr_shape].append(tmp)

shapes = {}
for k, v in shape_init.items():
    tmp = [
        frozenset((3 * i) + j for j in range(3) for i in range(3) if v[i][j] == "#"),
        frozenset(
            (3 * i) + (2 - j) for j in range(3) for i in range(3) if v[i][j] == "#"
        ),
        frozenset(
            (3 * (2 - i)) + (2 - j)
            for j in range(3)
            for i in range(3)
            if v[i][j] == "#"
        ),
        frozenset(
            (3 * (2 - i)) + j for j in range(3) for i in range(3) if v[i][j] == "#"
        ),
        frozenset((3 * j) + i for j in range(3) for i in range(3) if v[i][j] == "#"),
        frozenset(
            (3 * j) + (2 - i) for j in range(3) for i in range(3) if v[i][j] == "#"
        ),
        frozenset(
            (3 * (2 - j)) + (2 - i)
            for j in range(3)
            for i in range(3)
            if v[i][j] == "#"
        ),
        frozenset(
            (3 * (2 - j)) + i for j in range(3) for i in range(3) if v[i][j] == "#"
        ),
    ]
    shapes[k] = []
    for t in tmp:
        if len([1 for st in shapes[k] if t == st]) < 1:
            shapes[k].append(t)


@cache
def get_padded_shape(shape_variant, h_offset, w_offset, w):
    return frozenset(
        n + ((w - 3) * (n // 3)) + w_offset + h_offset * w for n in shape_variant
    )


@cache
def make_new_area(area, shape):
    return frozenset(area | shape), len(area & shape) > 0


@cache
def can_fit(cts, h, w, h_offset, w_offset, area):
    # need a better strategy of searching - no point in trying to put another
    # block into the same 3x3 block - should just keep moving to the right and trying out all shapes
    # that fit (instead of trying to get the counters down to 0 first)
    # precalc all possible new padded shapes or just go with the cache?
    # todo - broken - stopping as soon as there's an offset that yields nothing atm
    # print(cts, h_offset, w_offset)
    if sum(cts) == 0:
        return True
    elif h_offset > (h - 2):
        return False

    new_w = w_offset + 1
    h_updated = h_offset + (1 if new_w > w - 2 else 0)
    w_updated = 0 if new_w > w - 2 else new_w

    for i in range(6):
        if cts[i] > 0:
            for shape_variant in shapes[i]:
                (new_area, is_overlap) = make_new_area(
                    area,
                    get_padded_shape(
                        shape_variant,
                        h_offset,
                        w_offset,
                        w,
                    ),
                )
                if not is_overlap:
                    nums = list(cts)
                    nums[i] -= 1
                    return can_fit(
                        tuple(nums),
                        h,
                        w,
                        h_updated,
                        w_updated,
                        new_area,
                    )
    return can_fit(
        cts,
        h,
        w,
        h_updated,
        w_updated,
        area,
    )


p1 = 0
for a in areas:
    print(a)
    if can_fit(
        tuple(a[1]),
        a[0][0],
        a[0][1],
        0,
        0,
        frozenset(),
    ):
        p1 += 1
    get_padded_shape.cache_clear()
    make_new_area.cache_clear()
    can_fit.cache_clear()
    # break
print(p1)
