with open("input.txt", "r") as f:
    data = [[c for c in l.strip()] for l in f.readlines()]

rows = len(data)
cols = len(data[0])
check = [(i - 1, j - 1) for i in range(3) for j in range(3) if i != 1 or j != 1]

p1 = 0
for i in range(rows):
    for j in range(cols):
        if data[i][j] == "@":
            adjacent = 0
            for c in check:
                ci = i + c[0]
                cj = j + c[1]
                if (
                    ci >= 0
                    and cj >= 0
                    and ci < rows
                    and cj < cols
                    and data[ci][cj] == "@"
                ):
                    adjacent += 1
            if adjacent < 4:
                p1 += 1
print(p1)

new_data = [[c for c in r] for r in data]
p2 = 0
while True:
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == "@":
                adjacent = 0
                for c in check:
                    ci = i + c[0]
                    cj = j + c[1]
                    if (
                        ci >= 0
                        and cj >= 0
                        and ci < rows
                        and cj < cols
                        and data[ci][cj] == "@"
                    ):
                        adjacent += 1
                if adjacent < 4:
                    p2 += 1
                    new_data[i][j] = "."
    if new_data == data:
        break
    data = [[c for c in r] for r in new_data]
print(p2)
