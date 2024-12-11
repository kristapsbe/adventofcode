input = [int(c) for c in open("input.txt", "r").read().strip().split()]

print(input)

def brute_force_ftw(input, ct):
    for _ in range(ct):
        tmp = []
        for i in input:
            if i == 0:
                tmp.append(1)
            elif len(str(i))%2 == 0:
                si = str(i)
                sl = int(len(si)/2)
                tmp.append(int(si[:sl]))
                tmp.append(int(si[sl:]))
            else:
                tmp.append(i*2024)

        input = tmp
        #print(input)
    return input

print(brute_force_ftw(input, 25))
print(brute_force_ftw(input, 75))
