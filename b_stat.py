#!/usr/bin/python3

import sys
import glob
import re


def get(f, x):
    m = re.search(x + "(\\d+)", f)
    assert m is not None
    return int(m.groups()[0])


a = []
for f in glob.glob(f"{sys.argv[1]}/*.tsv"):
    with open(f) as fp:
        for l in fp:
            if "branch-misses" in l:
                l = l.strip()
                w = l.split("\t")
                bpredmiss = int(w[0])
                inner = get(f, "inner")
                nop = get(f, "nop")
                a.append((inner, nop, bpredmiss))

a.sort()

for x in a:
    print(*x, sep="\t")
