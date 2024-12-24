wires = {}
gates = {}
funs = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b
}

with open("input.txt", "r") as f:
    is_w = True
    for l in f.readlines():
        if l.strip() == "":
            is_w = False
            continue

        if is_w:
            p = l.strip().split(": ")
            wires[p[0]] = int(p[1])
        else:
            p = l.strip().split(" -> ")
            if p[1] not in wires and p[1] not in gates: # would have to filter later on anyhow, and can only set wires once - may as well skip
                gates[p[1]] = p[0].split()

while len(gates) > 0:
    tmp = {}
    for k, v in gates.items():
        if v[0] in wires and v[2] in wires:
            wires[k] = funs[v[1]](wires[v[0]], wires[v[2]])
        else:
            tmp[k] = v
    gates = tmp

r = 0
ct = 0
id = "z"+str(ct).zfill(2)
while id in wires:
    r += wires[id]*(2**ct)
    ct += 1
    id = "z"+str(ct).zfill(2)
print(r)
