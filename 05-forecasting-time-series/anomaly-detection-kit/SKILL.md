---
name: anomaly-detection-kit
description: Build practical anomaly detection for time series and streams — statistical baselines, seasonality-aware thresholds, alert design with precision/recall trade-offs. Activate when "something looks off" must become an automated signal.
---

# When to use
- Monitoring KPIs (revenue, traffic, error rates) for incidents
- Fraud/error detection in transaction streams
- Replacing static thresholds that fire constantly or never

# Process
1. **Define normal first** — profile the metric's baseline: level, trend, seasonality, variance; anomalies are deviations from THIS, not from zero.
2. **Method by data shape**:
   - Stationary metric → robust z-score (MAD)
   - Seasonal metric → STL residual monitoring or seasonal-hybrid ESD
   - Correlated metric group → multivariate (isolation forest, Mahalanobis) to catch "all metrics fine individually, weird together"
   - Streaming → rolling window EWMA with adaptive bands
3. **Threshold calibration** — tune against labeled history or simulated anomalies; report precision/recall of the detector itself; target alert volume humans can actually handle (≤ a few/day).
4. **Alert design** — severity tiers, persistence requirement (N consecutive breaches to avoid single-point noise), suppression during known events, runbook link per alert.
5. **Feedback loop** — log true/false positives from responders; re-tune monthly; retire detectors with no hits in 6 months.

# Inputs the skill needs
- Required: metric history, alerting channel, who responds
- Optional: labeled past incidents, known event calendar

# Output
- Working detector with calibrated thresholds
- Backtest report: precision/recall on historical incidents
- Alert spec (severity, persistence, runbook) ready for on-call

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/anomaly_detector.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/detection_design.md` - read before starting.
- `references/rca_framework.md` - structure your work with this framework

### assets/ - templates to fill and deliver
- `assets/detector_spec_template.md` - Fill this template - it IS the deliverable format.
