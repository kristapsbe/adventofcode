wires = {}
gates = {}
sgates = {}
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
            if p[1] not in wires: # would have to filter later on anyhow - may as well skip
                gates[p[1]] = p[0].split()
            sgates[p[1]] = sorted(p[0].split())

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

# x2 AND y2 -> a2
# x2 XOR y2 -> b2
#
# b2 AND d1 -> c2
# a2 OR c2 -> d2
# b2 XOR d1 -> z2
#
# 0 and N are special cases
# x0 AND y0 -> d0
# x0 XOR y0 -> z0
#
# xN AND yN -> aN
# xN XOR yN -> bN
#
# bN AND d(N-1) -> cN
# aN OR cN -> z(n+1)
# bN AND d(N-1) -> zN
def get_if_valid(i, m):
    xid = "x"+str(i).zfill(2)
    yid = "y"+str(i).zfill(2)
    zid = "z"+str(i).zfill(2)
    if i == 0:
        did = None
        for k,v in sgates.items():
            if v == ["AND", xid, yid]:
                did = k
                break
        if did is not None and sgates[zid] == ["XOR", xid, yid]:
            return {
                "z": zid,
                "d": did
            }
    else:
        aid = None
        bid = None
        cid = None
        zid = None
        did = None
        for k,v in sgates.items():
            if v == ["AND", xid, yid]:
                aid = k
            if v == ["XOR", xid, yid]:
                bid = k
        if aid is not None and bid is not None:
            cmatch = sorted(["AND", bid, valids[i-1]["d"]])
            zmatch = sorted(["XOR", bid, valids[i-1]["d"]])
            for k,v in sgates.items():
                if v == cmatch:
                    cid = k
                if v == zmatch:
                    zid = k
            if cid is not None:
                dmatch = sorted(["OR", aid, cid])
                for k,v in sgates.items():
                    if v == dmatch:
                        did = k
                        break
        print(i, aid, bid, cid, did, zid)
        if did is not None:
            return {
                "a": aid,
                "b": bid,
                "c": cid,
                "d": did,
                "z": zid
            }

    return None


# if it's stupid, but it works, it's not stupid, I suppose :D ...
swaps = [["z13", "vcv"], ["z19", "vwp"], ["z25", "mps"], ["vjv", "cqm"]]
for s in swaps:
    sgates[s[0]], sgates[s[1]] = sgates[s[1]], sgates[s[0]]

valids = []
for i in range(ct):
    e = get_if_valid(i, ct)
    if e is not None:
        valids.append(e)
    else:
        break

print(valids)

print(",".join(sorted([e for s in swaps for e in s])))
