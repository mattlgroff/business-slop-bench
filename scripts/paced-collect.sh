#!/bin/zsh
# zsh: macOS ships bash 3.2 without associative arrays.
# Collect one cell at a time, never calling the same model more often than once per GAP seconds.
# Anthropic routes on this Gateway account reject a second request to one model inside about six minutes.
# A 429 is recorded and never retried here; the model just waits an extra PENALTY seconds before its next cell.
set -u
cd "$(dirname "$0")/.."
GAP=${GAP:-420}; PENALTY=${PENALTY:-300}
MODELS=("$@")
[ ${#MODELS[@]} -gt 0 ] || { echo 'usage: paced-collect.sh model...' >&2; exit 2; }
TASKS=(pilot-client-email launch-delay-email vendor-decision-memo pilot-results-memo discovery-proposal change-order ai-strategy-slides handoff-slides)
typeset -A NEXTOK
for m in "${MODELS[@]}"; do NEXTOK[$m]=0; done
for task in "${TASKS[@]}"; do for cond in default house; do for m in "${MODELS[@]}"; do
  now=$(date +%s); wait=$(( ${NEXTOK[$m]} - now )); [ $wait -gt 0 ] && { echo "$(date -u +%FT%TZ) wait ${wait}s before $m"; sleep $wait; }
  out=$(npm run bench --silent -- collect "$m" "$task" "$cond" 2>&1); rc=$?
  line=$(printf '%s\n' "$out" | grep -E '^\{"id":' | head -1)
  if [ -n "$line" ]; then
    echo "$(date -u +%FT%TZ) $m $task $cond rc=$rc ${line:0:200}"
    now=$(date +%s); NEXTOK[$m]=$(( now + GAP ))
    printf '%s' "$line" | grep -q '"status":"error"' && NEXTOK[$m]=$(( now + GAP + PENALTY ))
  else
    echo "$(date -u +%FT%TZ) $m $task $cond rc=$rc no call (imported or existing): $(printf '%s\n' "$out" | grep -v '^{"model"' | tail -1 | cut -c1-160)"
  fi
done; done; done
echo "$(date -u +%FT%TZ) DONE"
