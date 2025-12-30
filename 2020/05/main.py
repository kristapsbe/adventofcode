with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

cmap = {
    "F": "0",
    "B": "1",
    "L": "0",
    "R": "1",
}

# Part 1
seats = [int("".join([cmap[c] for c in d]), 2) for d in data]
seats = sorted(seats)
print(seats[-1])

# Part 2
for x in range(len(seats)):
    if seats[x + 1] - seats[x] != 1:
        print(seats[x] + 1)
        break
