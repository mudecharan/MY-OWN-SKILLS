# API Ingestion Reference

## Reconnaissance checklist (before writing any client code)
- [ ] Pagination style: cursor (preferred) / offset / page-number? What marks the END?
- [ ] Rate limits: which headers (X-RateLimit-*)? Per-key or per-IP?
- [ ] Auth: token lifetime, refresh flow, scopes needed
- [ ] Incremental support: updated_at filter? webhooks? CDC feed?
- [ ] Field deprecation policy & versioning scheme
- [ ] Sandbox environment for testing

## Client rules
| Rule | Why |
|---|---|
| exponential backoff honoring Retry-After on 429/5xx | politeness + survival |
| request only needed fields | payload = cost × latency |
| persist high-water mark AFTER successful load only | crash-safe incrementality |
| overlap window by minutes + dedup | catches late commits |
| store raw JSON before parsing | re-parse when logic changes, no re-fetch |
| unknown fields tolerated in raw zone | schema drift ≠ outage |

## Incremental hierarchy
webhooks/CDC > updated_at cursor > ID chunking > full reload (small tables only)

## Daily smoke test
auth check + fetch 1 record per endpoint, run before business hours —
catches expired tokens at 6am instead of a broken dashboard at 9am.
