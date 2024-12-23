input = [l.strip().split("-") for l in open("input.txt", "r").readlines()]

connections = {}
for e in input:
    if e[0] not in connections:
        connections[e[0]] = [e[1]]
    else:
        connections[e[0]].append(e[1])

    if e[1] not in connections:
        connections[e[1]] = [e[0]]
    else:
        connections[e[1]].append(e[0])

groups = []
for k,v in connections.items():
    for i in range(len(v)-1):
        for j in range(i+1, len(v)):
            if v[i] in connections[v[j]]:
                g = sorted([k, v[i], v[j]])
                if g not in groups and len([e for e in g if "t" == e[0]]) > 0:
                    groups.append(g)

print(len(groups))

groups = {}
for k,v in connections.items():
    g = [k]
    tmp = v
    while True:
        rm = []
        for i in range(len(tmp)-1):
            for j in range(i+1, len(tmp)):
                if tmp[i] not in connections[tmp[j]]:
                    rm.append(i)
        if len(rm) == 0:
            g += tmp
            break
        else:
            tmp = [tmp[i] for i in range(len(tmp)) if i not in rm]

    sg = ",".join(sorted(g))
    if sg not in groups:
        groups[sg] = len(g)


print(max(groups, key=groups.get))
