import re

from decimal import Decimal as D


input = []
with open("input.txt", "r") as f:
    entry = {}
    for l in f.readlines():
        ls = l.strip()
        if ls == "":
            input.append(entry)
            entry = {}
        else:
            p = ls.split()
            entry[" ".join(p[:-2])] = {re.split(r'=|\+', pe)[0]: D(re.split(r'=|\+', pe.replace(",", ""))[1]) for pe in p[-2:]}
    input.append(entry)

a_cost = 3
b_cost = 1


def solve(input, part_two=False):
    costs = []
    for i in input:
        if part_two:
            i["Prize:"]["X"] += D(10000000000000)
            i["Prize:"]["Y"] += D(10000000000000)

        b = i["Button A:"]["X"]*(((i["Prize:"]["X"]*i["Button A:"]["Y"])/i["Button A:"]["X"])-i["Prize:"]["Y"])/(i["Button A:"]["Y"]*i["Button B:"]["X"]-i["Button A:"]["X"]*i["Button B:"]["Y"])
        a = (i["Prize:"]["X"]-b*i["Button B:"]["X"])/i["Button A:"]["X"]

        if b >= 0 and abs(round(b, 6)-b) < D(0.000000001) and a >= 0 and abs(round(a, 6)-a) < D(0.000000001):
            costs.append(round(a)*a_cost+round(b)*b_cost)
    return costs

print(sum(solve(input)))
print(sum(solve(input, True)))
