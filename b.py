#!/usr/bin/python3

import string
import sys

with open("b.s") as fp:
    t = fp.read()

templ = string.Template(t)

inner, outer, nopc, nop2c = sys.argv[1:]
nopc = int(nopc)
nop2c = int(nop2c)
nop = "\n".join(["\tnop"] * nopc)
nop2 = "\n".join(["\tnop"] * nop2c)
s = templ.substitute(inner=inner, outer=outer, nop=nop, nop2=nop2)

print(s)
