input = [int(c) for c in list(open("input.txt", "r").read().strip())]

filled = []
do_fill = True
fw = 0
bk = len(input)//2*2
bki = input[bk]
while fw <= bk:
    if do_fill:
        filled += [fw/2 for _ in range(input[fw])]
        fw += 2
    else:
        t = input[fw-1]
        f = 0
        while f < t and fw <= bk:
            if fw == bk:
                filled += [bk/2 for _ in range(bki)]
                bk -= 2
            elif f+bki > t:
                bki = bki-(t-f)
                filled += [bk/2 for _ in range(t-f)]
                f += (t-f)
            else:
                filled += [bk/2 for _ in range(bki)]
                f += bki
                bk -= 2
                bki = input[bk]
    do_fill = not do_fill

checksum = []
for i in range(len(filled)):
    checksum.append(i*filled[i])
print(int(sum(checksum)))

filled = []
bk = len(input)//2*2
moved = {}
gaps = [input[i] for i in range(len(input)) if i%2 == 1]
gl = len(gaps)
non_gaps = [input[i] for i in range(len(input)) if i%2 == 0]
ngl = len(non_gaps)
for i in range(len(non_gaps)):
    for j in range(gl-i):
        if gaps[j] >= non_gaps[-(i+1)]:
            gaps[j] -= non_gaps[-(i+1)]
            moved[ngl-(i+1)] = j
            break

checksum = []
for i in range(len(input)):
    ct = sum(input[:i])
    if i%2 == 0:
        if i//2 not in moved:
            for j in range(input[i]):
                checksum.append(i//2*(ct+j))
    else:
        ict = 0
        for k,v in moved.items():
            if i//2 == v:
                for j in range(input[k*2]):
                    checksum.append(k*(ct+ict))
                    ict += 1
print(int(sum(checksum)))
