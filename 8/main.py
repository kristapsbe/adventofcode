import math
# https://adventofcode.com/2023/day/8


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/8/input
    lines = f.read().split("\n")

instr = lines[0]
imap = {"L": 0, "R": 1}
nodes = {l.split("=")[0].strip(): [d.strip() for d in l.split("(")[1].split(")")[0].split(",")] for l in lines[1:] if l.strip() != ""}

# PART ONE
cnode = "AAA"
fnode = "ZZZ"
ct = 0
while cnode != fnode:
    d = instr[ct%len(instr)]
    cnode = nodes[cnode][imap[d]]
    ct = ct + 1

print(f"PART ONE: {ct}")

# PART TWO
# I get that this works because, e.g. ny input has 6 starts and ends that are part of unique circles (and map to the same pair of nodes)
# QXA = (LSB, MQN) => HLZ = (MQN, LSB)
# PDA = (NVV, MSV) => XBZ = (MSV, NVV)
# TDA = (CFN, PVL) => VJZ = (PVL, CFN)
# QQA = (QHT, BDJ) => PXZ = (BDJ, QHT)
# PPA = (SLK, QLG) => NBZ = (QLG, SLK)
# AAA = (BNG, RLN) => ZZZ = (RLN, BNG)
# but I'd still much prefer if I could come up with a reasonable quick solution that doesn't rely on this being true
cnodes = [k for k in nodes.keys() if k[-1] == "A"]
ct = 0
cts = []
while len([c for c in cnodes if c[-1] != "Z"]) > 0:
    d = instr[ct%len(instr)]	
    ct = ct + 1
    tmp = []
    for c in cnodes:
        if c[-1] != "Z":
            tmp_c = nodes[c][imap[d]] 
            if tmp_c[-1] == "Z":
                cts.append(ct) # we found a new end of the circle - store length
            tmp.append(tmp_c)
        else:
            tmp.append(c)
    cnodes = tmp

print(f"PART TWO: {math.lcm(*cts)}")