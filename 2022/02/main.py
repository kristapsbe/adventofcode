with open("input.txt", "r") as f:
    data = [e.strip().split() for e in f.readlines()]

beats = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

ties = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

values = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

p1 = 0
for m in data:
    outcome = 0
    if m[1] == beats[m[0]]:
        outcome = 6
    if m[1] == ties[m[0]]:
        outcome = 3
    p1 += values[m[1]] + outcome
print(p1)

loses = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

p2 = 0
for m in data:
    match m[1]:
        case "X":
            p2 += values[loses[m[0]]]
        case "Y":
            p2 += values[ties[m[0]]] + 3
        case "Z":
            p2 += values[beats[m[0]]] + 6
print(p2)
