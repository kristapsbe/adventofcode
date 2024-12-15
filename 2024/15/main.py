walls = []
boxes = set()
dirs = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}
moves = []
robot = (0, 0)
w = -1
h = -1
fname = "input.txt"


with open(fname, "r") as f:
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


def draw(p2=False):
    ih = h+1
    iw = w
    if p2:
        iw *= 2

    print()
    for i in range(ih):
        r = ""
        for j in range(iw):
            if (i, j) in walls:
                r += "#"
            elif (i, j) in boxes:
                r += "O"
            elif (i, j, j+1) in boxes:
                r += "[]"
            elif (i, j-1, j) in boxes:
                pass
            elif (i, j) == robot:
                r += "@"
            else:
                r += "."
        print(r)


for m in moves:
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

walls = []
boxes = set()
moves = []
with open(fname, "r") as f:
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
                        walls.append((i, 2*j))
                        walls.append((i, 2*j+1))
                    case "O":
                        boxes.add((i, 2*j, 2*j+1))
                    case "@":
                        robot = (i, 2*j)
                j += 1
        i += 1


for m in moves:
    #draw(True)
    #print(m)
    #input()

    tmp_robot = (robot[0]+m[0], robot[1]+m[1])
    if tmp_robot not in walls:
        moved_boxes = set(b for b in boxes if b[0] == tmp_robot[0] and (b[1] == tmp_robot[1] or b[2] == tmp_robot[1]))

        if len(moved_boxes) == 0:
            robot = tmp_robot
        else:
            boxes_to_move = moved_boxes
            do_move = False
            while True:
                if len([mb for mb in boxes_to_move if (mb[0]+m[0], mb[1]+m[1]) in walls or (mb[0]+m[0], mb[2]+m[1]) in walls]) > 0:
                    break
                elif len(boxes_to_move) > 0:
                    tmp_boxes_to_move = set()
                    for b in boxes_to_move:
                        tmp_b = (b[0]+m[0], b[1]+m[1], b[2]+m[1])
                        for b1 in boxes:
                            if tmp_b[0] == b1[0] and (tmp_b[1] == b1[1] or tmp_b[1] == b1[2] or tmp_b[2] == b1[1]) and b1 not in boxes_to_move:
                                tmp_boxes_to_move.add(b1)
                    for b in boxes_to_move:
                        moved_boxes.add(b)
                    #print(boxes_to_move, tmp_boxes_to_move)
                    if boxes_to_move == tmp_boxes_to_move:
                        quit()
                    boxes_to_move = tmp_boxes_to_move
                else:
                    do_move = True
                    break
            if do_move:
                for b in moved_boxes:
                    boxes.remove(b)
                for b in moved_boxes:
                    boxes.add((b[0]+m[0], b[1]+m[1], b[2]+m[1]))
                robot = tmp_robot

#draw(True)
#print([{b: [b[0], h-b[0], h, b[1], 2*w-b[2]-1, w]} for b in boxes])
print(sum([b[0]*100+b[1] for b in boxes]))
