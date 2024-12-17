from math import floor
pointer = 0

registers = {
    "A": 0,
    "B": 0,
    "C": 0
}

program = []

combo = [
    lambda o: o,
    lambda o: o,
    lambda o: o,
    lambda o: o,
    lambda o: registers["A"],
    lambda o: registers["B"],
    lambda o: registers["C"],
]

otp = []


def dv(r, o):
    return int(floor(r/(2**combo[o](o))))# % 2147483647 # truncate to int


def adv(o, p, r, otp):
    r["A"] = dv(r["A"], o)
    return p+2, r, otp


def bxl(o, p, r, otp):
    r["B"] = r["B"] ^ o
    return p+2, r, otp


def bst(o, p, r, otp):
    r["B"] = combo[o](o)%8
    return p+2, r, otp


def jnz(o, p, r, otp):
    return o if r["A"] > 0 else p+2, r, otp


def bxc(o, p, r, otp):
    r["B"] = r["B"] ^ r["C"]
    return p+2, r, otp


def out(o, p, r, otp):
    return p+2, r, otp+[combo[o](o)%8]


def bdv(o, p, r, otp):
    r["B"] = dv(r["A"], o)
    return p+2, r, otp


def cdv(o, p, r, otp):
    r["C"] = dv(r["A"], o)
    return p+2, r, otp


instructs = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

with open("input.txt", "r") as f:
    for l in f.readlines():
        parts = l.strip().split(" ")[-1].split(",")
        if "Register A" in l:
            registers["A"] = int(parts[0])
        elif "Register B" in l:
            registers["B"] = int(parts[0])
        elif "Register C" in l:
            registers["C"] = int(parts[0])
        elif "Program" in l:
            program = [int(o) for o in parts]

#print(pointer, program, registers, otp)
while pointer < len(program):
    pointer, registers, otp = instructs[program[pointer]](program[pointer+1], pointer, registers, otp)
    #print(pointer, program, registers, otp)
    #input()

#print(registers)
#print(program)
#print(pointer)
print(",".join([str(o) for o in otp]))

reg_a = 0

while otp != program:
    reg_a += 1
    registers = {
        "A": reg_a,
        "B": 0,
        "C": 0
    }
    pointer = 0
    otp = []

    while pointer < len(program) and otp == program[:len(otp)]:
        pointer, registers, otp = instructs[program[pointer]](program[pointer+1], pointer, registers, otp)
    #print(reg_a, otp)
    #input()
    if reg_a % 777777 == 0:
        print(reg_a, otp, program)

print(reg_a)
