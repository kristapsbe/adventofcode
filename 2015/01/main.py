with open("input.txt", "r") as f:
    input = f.read()

p1 = input.count("(") - input.count(")")

print(p1)

pos = 0
p2 = 0
for c in input:
    p2 += 1
    if c == "(":
        pos += 1
    else:
        pos -= 1
    if pos < 0:
        break
print(p2)
