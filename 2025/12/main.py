import json
from functools import cache
from operator import is_

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
def get_padded_shape(shape_variant, offset_h, offset_w, w):
    # print(
    #     shape_variant,
    #     offset_h,
    #     offset_w,
    #     frozenset(
    #         n + ((w - 3) * n // 3) + offset_w + offset_h * w for n in shape_variant
    #     ),
    #     "test shape",
    # )
    return frozenset(
        n + ((w - 3) * (n // 3)) + offset_w + offset_h * w for n in shape_variant
    )


@cache
def make_new_area(area, shape):
    return frozenset(area | shape), len(area & shape) > 0


@cache
def can_fit(cts, h, w, area):
    # need a better strategy of searching - no point in trying to put another
    # block into the same 3x3 block - should just keep moving to the right and trying out all shapes
    # that fit (instead of trying to get the counters down to 0 first)
    # precalc all possible new padded shapes or just go with the cache?
    if sum(cts) == 0:
        # print(area, "AAAA")
        return True
    for i in range(6):
        if cts[i] > 0:
            for j in range(h - 2):
                for k in range(w - 2):
                    for sss, shape_variant in enumerate(shapes[i]):
                        (new_area, is_overlap) = make_new_area(
                            area,
                            get_padded_shape(
                                shape_variant,
                                j,
                                k,
                                w,
                            ),
                        )
                        if not is_overlap:
                            nums = list(cts)
                            nums[i] -= 1
                            return can_fit(tuple(nums), h, w, new_area)
                            # tmp_num = get_padded_shape(
                            #     shape_variant,
                            #     j,
                            #     k,
                            #     w,
                            # )
                            # print(
                            #     tmp_num,
                            #     tuple(nums),
                            #     "CCCC",
                            # )
                            # print("==", i, sss)

                            # for ih in range(3):
                            #     print(
                            #         [
                            #             int(iw + 3 * ih in shape_variant)
                            #             for iw in range(3)
                            #         ]
                            #     )
                            # for ih in range(h):
                            #     print(
                            #         [int(iw + w * ih in tmp_num) for iw in range(w)]
                            #     )
                            # return True
    # print(cts, "BBBB")
    return False


p1 = 0
for a in areas:
    print(a)
    if can_fit(
        tuple(a[1]),
        a[0][0],
        a[0][1],
        frozenset(),
    ):
        p1 += 1
    # break
print(p1)
