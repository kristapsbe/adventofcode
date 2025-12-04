with open("input.txt", "r") as f:
    instructions = [d.strip() for d in f.read().split(",")]

curr_coords = [0, 0]
turn = {"R": 1, "L": -1}
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dir = 0

for i in instructions:
    t = i[0]
    dist = int(i[1:])

    dir += turn[t]
    curr_dir = dirs[dir % len(dirs)]
    curr_coords[0] += curr_dir[0] * dist
    curr_coords[1] += curr_dir[1] * dist

print(abs(curr_coords[0]) + abs(curr_coords[1]))

curr_coords = [0, 0]
dir = 0
visited = set()

for i in instructions:
    t = i[0]
    dist = int(i[1:])

    dir += turn[t]
    curr_dir = dirs[dir % len(dirs)]

    do_break = False
    for i in range(dist):
        curr_coords[0] += curr_dir[0]
        curr_coords[1] += curr_dir[1]

        cc = (curr_coords[0], curr_coords[1])
        if cc in visited:
            do_break = True
            break
        visited.add(cc)
    if do_break:
        break

print(abs(curr_coords[0]) + abs(curr_coords[1]))
