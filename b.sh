#!/bin/bash

set -euo pipefail
set -x

for n in $(seq 0 8); do
for i in $(seq 1 64); do
  j=$((2 ** 15 / i))
  python3 b.py ${i} ${j} ${n} >/tmp/a.s
  gcc /tmp/a.s
  time ./a.out
done
done
