#!/bin/bash

set -euo pipefail
set -x

HOST=$(hostname)
mkdir -p ${HOST} ${HOST}_br

OUT=${HOST}
OUT_BR=${HOST}_br

INNER_MAX=128
if [[ ${HOST} == "raspi5" ]]; then
  INNER_MAX=$((128 * 3))
fi

for n in $(seq 0 8); do
  for n2 in $(seq 0 8); do
    for i in $(seq 1 ${INNER_MAX}); do
      j=$((2 ** 15 / i))
      python3 b.py "${i}" "${j}" "${n}" "${n2}" >/tmp/a.s
      gcc /tmp/a.s b.c
      perf stat -ddd -x'\t' -o "${OUT}/perf.inner${i}.outer${j}.nop${n}.nop2${n2}.tsv" ./a.out >"${OUT}/inner${i}.outer${j}.nop${n}.nop2${n2}.stdout"
      objdump -d a.out >"${OUT}/inner${i}.outer${j}.nop${n}.nop2${n2}.objdump"

      python3 b.py "${i}" "${j}" "${n}" "${n2}" --use_br >/tmp/a.s
      gcc /tmp/a.s b.c
      perf stat -ddd -x'\t' -o "${OUT_BR}/perf.inner${i}.outer${j}.nop${n}.nop2${n2}.tsv" ./a.out >"${OUT_BR}/inner${i}.outer${j}.nop${n}.nop2${n2}.stdout"
      objdump -d a.out >"${OUT_BR}/inner${i}.outer${j}.nop${n}.nop2${n2}.objdump"
    done
  done
done
