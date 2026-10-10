# Focused recovery corrective

FAB-08: browser failure leaves draft open but persistent simulation switch is
behind native modal. Expected: retry reachable without discarding draft.
One fresh Prototype context; no full pipeline, no domain/rule/identity changes.
Source/cache beta8, 57 files, 27ff6de3cf87a07d. Forecast 250000 input/7000 output,
max600 seconds; forecast is not a hard token limiter. Root browser observes
actual failure-retained draft-retry-result, separately from harness proof.
Original failed candidate and AX/screenshot frozen. Exactly one reset allowed,
zero used. No general prototype/usability/native mobile PASS.
