---
name: seasonality-detector
description: Identify and quantify seasonality, trend, and cycles in time series — decomposition, periodograms, holiday effects, calendar artifacts — and decide what to model vs adjust for. Activate when patterns repeat but aren't understood.
---

# When to use
- "Is this dip seasonal or a real problem?"
- Preparing series for forecasting or anomaly detection
- Setting targets that respect natural cycles

# Process
1. **Visual decomposition** — STL decomposition (robust to outliers) at candidate periods; inspect trend, seasonal, remainder panels separately.
2. **Period verification** — autocorrelation/ACF peaks, periodogram (Fourier) power, and day-of-week/month-of-year group means; confirm the true dominant period (weekly? 4-4-5 retail calendar? lunar?).
3. **Amplitude quantification** — seasonal strength metric (Wang-Smith-Hyndman); express as % of level ("Fridays run +22% above average").
4. **Calendar effects** — holiday shifts, working-day counts, payday effects, leap years; distinguish calendar artifacts from true seasonality.
5. **Evolving seasonality** — test if seasonal pattern changes over years (rolling STL); non-stationary seasonality needs dynamic handling.
6. **Decision guidance** — for reporting: seasonally-adjust series; for forecasting: explicit seasonal terms; for anomaly detection: detect on seasonally-adjusted residuals.

# Inputs the skill needs
- Required: time series with timestamps, suspected business cycles
- Optional: holiday calendars, known one-off events to mask

# Output
- Decomposition plots + verified seasonal periods
- Quantified seasonal profile (e.g., index by day/month)
- Recommendation: adjust, model, or monitor per use case

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/seasonality_scan.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/seasonality_reference.md` - read before executing the Process
- `references/ts_patterns_guide.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/seasonality_findings_template.md` - Fill this template - it IS the deliverable format.
