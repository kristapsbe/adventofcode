input = [int(c) for c in open("input.txt", "r").read().strip().split()]

print(input)

def memoize(func):
    cache = {}
    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return inner

@memoize
def calc_len(i, d):
    i_len_mod = len(str(i)) % 2
    if d == 1:
        return 2 - i_len_mod
    else:
        if i == 0:
            return calc_len(1, d-1)
        elif i_len_mod == 0:
            si = str(i)
            sl = int(len(si)/2)
            return calc_len(int(si[:sl]), d-1) + calc_len(int(si[sl:]), d-1)
        else:
            return calc_len(i*2024, d-1)


print(sum([calc_len(i, 25) for i in input]))
print(sum([calc_len(i, 75) for i in input]))
