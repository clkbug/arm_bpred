#!/usr/bin/python3

import string
import sys

with open("b.s") as fp:
    t = fp.read()

templ = string.Template(t)

inner, outer, nopc = sys.argv[1:]
nopc = int(nopc)
nop = "\n".join(["nop"] * nopc)
s = templ.substitute(inner = inner, outer = outer, nop = nop)

print(s)

