#!/usr/bin/python3

import string
import sys
import random

with open("b.s") as fp:
    t = fp.read()

templ = string.Template(t)

inner, outer, nopc, nop2c = sys.argv[1:5]
nopc = int(nopc)
nop2c = int(nop2c)
nop = "\n".join(["\tnop"] * nopc)
nop2 = "\n".join(["\tnop"] * nop2c)

if "--use_br" in sys.argv:
    order = [i for i in range(1, nop2c)]
    random.shuffle(order)
    order.insert(0, 0)
    order.append(nop2c)

    a = [-1] * nop2c

    for i in range(nop2c):
        a[order[i]] = order[i+1]
    s = ""
    # s = "\tsub x4, x2, x3"
    s += f"\tcmp x2, x3\n"
    for i in range(nop2c):
        s += f".temporal_branch{i}:\n"
        s += f"\tb.ls .temporal_branch{a[i]}\n"
    s += f".temporal_branch{nop2c}:"

    nop2 = s

s = templ.substitute(inner=inner, outer=outer, nop=nop, nop2=nop2)

print(s)
