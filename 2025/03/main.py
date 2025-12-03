with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

p1 = 0
p2 = 0
for l in data:
    max_i = max([int(i) for i in l[:-1]])
    max_j = max([int(j) for j in l[l.index(f"{max_i}") + 1 :]])
    p1 += 10 * max_i + max_j

    num_len = 12
    big_j = [max([int(i) for i in l[: -(num_len - 1)]])]
    tmp_l = l
    for c in range(2, num_len + 1):
        tmp_l = tmp_l[tmp_l.index(f"{big_j[-1]}") + 1 :]
        use_l = tmp_l[: -(num_len - c)] if c != num_len else tmp_l
        big_j.append(max([int(j) for j in use_l]))
    p2 += int("".join([str(n) for n in big_j]))
print(p1)
print(p2)
