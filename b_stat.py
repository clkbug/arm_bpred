#!/usr/bin/python3

import sys
import glob
import re
import pandas


def get(f, x):
    m = re.search(x + "(\\d+)", f)
    assert m is not None
    return int(m.groups()[0])


def branch_addr(filename):
    ret = {}
    with open(filename) as fp:
        curFun = ""
        for l in fp:
            # print(curFun)
            if ">:" in l:
                curFun = l.split("<")[1].replace(">:", "").strip()
                continue
            if curFun == ".loop_inner" and "cbnz" in l:
                ret["br1"] = int(l.strip().split(":")[0], base=16)
            if curFun == ".loop_outer" and "cbnz" in l:
                ret["br2"] = int(l.strip().split(":")[0], base=16)
    return ret


a = []
for f in glob.glob(f"{sys.argv[1]}/*.tsv"):
    asm = "asm/" + f.split("/")[1].replace("perf.",
                                           "").replace(".tsv", ".objdump")
    data = branch_addr(asm)
    with open(f) as fp:
        data["inner"] = get(f, "inner")
        data["outer"] = get(f, "outer")
        data["nop"] = get(f, "nop")
        data["nop2"] = get(f, "nop2")
        for i, l in enumerate(fp):
            if i < 2:
                continue
            w = l.split("\t")
            k = w[2].replace(":u", "").replace("-", "_")
            v = w[0] if w[0] != "<not supported>" else "NA"
            data[k] = v
        a.append(data)

df = pandas.DataFrame.from_records(a)
df.to_csv(sys.stdout, sep="\t", index=False)
