with open("input.txt", "r") as f:
    jumps = [int(c.strip()) for c in f.readlines()]

pos = 0
max_pos = len(jumps)
p1 = 0
while pos >= 0 and pos < max_pos:
    p1 += 1
    jump_val = jumps[pos]
    jumps[pos] += 1
    pos += jump_val
print(p1)

with open("input.txt", "r") as f:
    jumps = [int(c.strip()) for c in f.readlines()]

pos = 0
max_pos = len(jumps)
p2 = 0
while pos >= 0 and pos < max_pos:
    p2 += 1
    jump_val = jumps[pos]
    if jump_val >= 3:
        jumps[pos] -= 1
    else:
        jumps[pos] += 1
    pos += jump_val
print(p2)
