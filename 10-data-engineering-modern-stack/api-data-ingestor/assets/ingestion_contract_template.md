# Ingestion Contract — <source API>

## Source facts (from docs + probes)
| Item | Value |
|---|---|
| Base URL / version | |
| Auth flow & token lifetime | |
| Pagination style & end-marker | |
| Rate limit & headers | |
| Incremental field | |
| Webhook available? | |

## Output contract
| Item | Value |
|---|---|
| Landing table + grain | |
| Freshness SLA | |
| Completeness SLA vs trailing avg | ±__% |
| Schema drift policy (alert on add; fail on remove) | |

## State management
High-water mark storage: ____ · advanced only after successful load ☐
Backfill procedure: parameterized windows, throttled to __ req/sec

## Monitoring
- [ ] daily smoke test 06:00 UTC (auth + 1 record/endpoint)
- [ ] freshness alert at SLA breach
- [ ] volume anomaly alert (±40% vs 7-day avg)

## Runbook pointer & owner
Owner: ____ · Runbook: ____
