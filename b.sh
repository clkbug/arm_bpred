#!/bin/bash

set -euo pipefail
set -x

for n in $(seq 0 8); do
  for n2 in $(seq 0 8); do
    for i in $(seq 1 128); do
      j=$((2 ** 15 / i))
      python3 b.py ${i} ${j} ${n} ${n2} >/tmp/a.s
      gcc /tmp/a.s b.c
      perf stat -ddd -x'\t' -o perf.inner${i}.outer${j}.nop${n}.nop2${n2}.tsv ./a.out >inner${i}.outer${j}.nop${n}.nop2${n2}.stdout
      objdump -d a.out >inner${i}.outer${j}.nop${n}.nop2${n2}.objdump
    done
  done
done
