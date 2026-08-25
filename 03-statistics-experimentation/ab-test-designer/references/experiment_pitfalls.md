# Experimentation Pitfall Reference

## Sample Ratio Mismatch (SRM) — the #1 silent killer
If a 50/50 test lands 49/51 over 100k users, something is broken (bots, redirects,
instrumentation). A significant SRM invalidates ALL downstream numbers.
Check: chi-square of observed counts vs intended split; p < 0.001 = alarm.

## Peeking
Checking daily and shipping on first p<0.05 inflates false positives massively
(~25% at 5 checks vs 5% nominal). Fixes: fixed horizon, group-sequential bounds,
or Bayesian expected-loss stopping.

## Common metric traps
- Ratio metrics (CTR, AOV) need delta-method or bootstrap SEs, not naive z-tests.
- Count metrics per user need user-level randomization + user-level analysis.
- Novelty effects: effect decays after week 1 — always split by cohort week.
- Twyman's law: any surprising extreme result is usually a bug. Verify instrumentation.

## Randomization hygiene
- Salt hashes per experiment so users can be in different arms across tests.
- Unit of assignment = unit of analysis (user, not session/pageview).
- Exclusions decided BEFORE looking at outcomes; post-hoc filtering biases results.

## Guardrails to consider by default
Latency, error rates, unsubscribe/opt-out, support contacts, downstream conversion.
