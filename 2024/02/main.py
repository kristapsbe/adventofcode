reports = [[int(e) for e in l.split()] for l in open("input.txt", "r").readlines()]

max_min = range(1, 4)

adj = [list(map(lambda e: e[0]-e[1], zip(r, r[1:]))) for r in reports]
def is_safe(a):
    return 1 if abs(sum([max(-1, min(1, e if abs(e) in max_min else 0)) for e in a])) == len(a) else 0

print(sum([is_safe(a) for a in adj]))

all_reports = [[r[:i]+r[i+1:] for i in range(len(r))]+[r] for r in reports]
adj = [[list(map(lambda e: e[0]-e[1], zip(r, r[1:]))) for r in ar] for ar in all_reports]
print(sum([max([is_safe(e) for e in a]) for a in adj]))
