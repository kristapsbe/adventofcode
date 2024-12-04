text = open("input.txt", "r").readlines()

h = len(text)
w = len(text[0])

xmas = "XMAS"
dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def find_xmas(i, j, xmas, dir):
    if len(xmas) == 0:
        return 1
    else:
        if i >= 0 and i < h and j >= 0 and j < w and text[i][j] == xmas[0]:
            return find_xmas(i+dir[0], j+dir[1], xmas[1:], dir)
        else:
            return 0

ct = 0
for i in range(h):
    for j in range(w):
        for dir in dirs:
            ct += find_xmas(i, j, xmas, dir)
print(ct)

ct = 0
for i in range(1, h-1):
    for j in range(1, w-1):
        if text[i][j] == "A" and ((text[i-1][j-1] == "M" and text[i+1][j+1] == "S") or (text[i-1][j-1] == "S" and text[i+1][j+1] == "M")) and ((text[i-1][j+1] == "M" and text[i+1][j-1] == "S") or (text[i-1][j+1] == "S" and text[i+1][j-1] == "M")):
            ct += 1
print(ct)
