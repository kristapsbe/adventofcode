with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

keypad1 = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

keypad2 = [
    ["","","1","",""],
    ["","2","3","4",""],
    ["5","6","7","8","9"],
    ["","A","B","C",""],
    ["","","D","",""],
]

pos1 = [1, 1]
pos2 = [2, 0]

moves = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

p1 = ""
p2 = ""
for l in data:
    for c in l:
        tmp_pos2 = [p for p in pos2]
        for i in range(2):
            pos1[i] = min(max(0, pos1[i]+moves[c][i]), 2)
            tmp_pos2[i] = min(max(0, pos2[i]+moves[c][i]), 4)
        if keypad2[tmp_pos2[0]][tmp_pos2[1]] != "":
            pos2 = [p for p in tmp_pos2]
    p1 += keypad1[pos1[0]][pos1[1]]
    p2 += keypad2[pos2[0]][pos2[1]]

print(p1)
print(p2)
