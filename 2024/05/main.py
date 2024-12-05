text = open("input.txt", "r").readlines()

rules = {}
updates = []
for e in text:
    if "|" in e:
        parts = [int(n) for n in e.split("|")]
        if parts[0] not in rules:
            rules[parts[0]] = []
        rules[parts[0]].append(parts[1])
    elif "," in e:
        updates.append([int(n) for n in e.split(",")])


def is_valid_order(update, rules):
    if len(update) == 0:
        return True
    elif len([u for u in update if update[-1] in rules and u in rules[update[-1]]]):
        return False
    return is_valid_order(update[:-1], rules)


print(rules)

#quit()
#print(updates)
middles = []
for u in updates:
    if is_valid_order(u, rules):
        middles.append(u[len(u)//2])
#print(middles)
print(sum(middles))


def is_smallest(ki, vi, num_map, rules):
    for kj, vj in rules.items():
        if ki != kj and kj not in num_map and ki in vj:
            return False
    return True

middles = []
for u in updates:
    if not is_valid_order(u, rules):
        tmp_rules = {k: v for k, v in rules.items() if k in u}
        num_map = {}
        while (len(num_map) < len(tmp_rules)):
            for ki, vi in tmp_rules.items():
                if ki not in num_map and is_smallest(ki, vi, num_map, tmp_rules):
                    num_map[ki] = len(num_map)
            print(f"{len(num_map)} < {len(tmp_rules)}")
        print(num_map)

        middles.append([x for _, x in sorted(zip([num_map.get(e, len(num_map)) for e in u], u))][len(u)//2])
print(sum(middles))
