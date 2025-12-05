ranges = []
ingredients = []

with open("input.txt", "r") as f:
    for l in f.readlines():
        s = l.strip()
        if s:
            if "-" in s:
                parts = s.strip().split("-")
                ranges.append((int(parts[0]), int(parts[1])))
            else:
                ingredients.append(int(s.strip()))

p1 = 0
for i in ingredients:
    for r in ranges:
        if i >= r[0] and i <= r[1]:
            p1 += 1
            break
print(p1)

p2 = 0
while True:
    overlapped_ids = set()
    min_val = 0
    max_val = 0
    num_ranges = len(ranges)
    for i in range(num_ranges):
        min_val = ranges[i][0]
        max_val = ranges[i][1]
        overlapped_ids = set([i])
        for j in range(i, num_ranges):
            c_min = ranges[j][0]
            c_max = ranges[j][1]
            if c_min <= min_val and c_max >= max_val:
                max_val = c_max
                min_val = c_min
                overlapped_ids.add(j)
            else:
                if min_val <= c_min and max_val >= c_min:
                    max_val = max(max_val, c_max)
                    overlapped_ids.add(j)
                if min_val <= c_max and max_val >= c_max:
                    min_val = min(min_val, c_min)
                    overlapped_ids.add(j)

        if len(overlapped_ids) >= 2:
            break

    if len(overlapped_ids) < 2:
        break
    ranges = [ranges[i] for i in range(num_ranges) if i not in overlapped_ids]
    ranges.append((min_val, max_val))

for r in ranges:
    p2 += r[1] - r[0] + 1
print(p2)
