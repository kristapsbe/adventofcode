walls = []
boxes = set()
dirs = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}
moves = []
robot = (0, 0)
w = -1
h = -1

with open("input.txt", "r") as f:
    is_moves = False
    i = 0
    for l in f.readlines():
        if is_moves:
            for c in l.strip():
                moves.append(dirs[c])
        else:
            if l.strip() == "":
                is_moves = True
                continue

            j = 0
            for c in l.strip():
                match c:
                    case "#":
                        walls.append((i, j))
                    case "O":
                        boxes.add((i, j))
                    case "@":
                        robot = (i, j)
                j += 1

            w = j
            h = i
        i += 1

def draw():
    print()
    for i in range(h+1):
        r = ""
        for j in range(w):
            if (i, j) in walls:
                r += "#"
            elif (i, j) in boxes:
                r += "O"
            elif (i, j) == robot:
                r += "@"
            else:
                r += "."
        print(r)

for m in moves:
    #draw()
    tmp_robot = (robot[0]+m[0], robot[1]+m[1])
    if tmp_robot not in walls:
        if tmp_robot not in boxes:
            robot = tmp_robot
        else:
            tmp_moved_box = (tmp_robot[0]+m[0], tmp_robot[1]+m[1])
            while True:
                if tmp_moved_box in walls:
                    break
                elif tmp_moved_box in boxes:
                    tmp_moved_box = (tmp_moved_box[0]+m[0], tmp_moved_box[1]+m[1])
                else:
                    boxes.remove(tmp_robot)
                    boxes.add(tmp_moved_box)
                    robot = tmp_robot
                    break

print(sum([b[0]*100+b[1] for b in boxes]))
