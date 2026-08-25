# Data Project Skills Library — 54 Skills

A portable library of **54 SKILL.md packages** that turn any AI coding agent into an advanced data professional across data analytics, data science, business analysis, engineering, finance/risk, and reporting. Each skill is self-contained: activate it alone and it drives a complete advanced project — reading its `references/`, running its `scripts/`, and filling its `assets/` templates as deliverables.

Every skill folder follows the same layout:

```
<category>/<skill-name>/
├── SKILL.md        # workflow + Execution Protocol (read refs → run scripts → fill assets)
├── scripts/        # runnable Python / SQL tools
├── references/     # method guides, decision trees, checklists
└── assets/         # report/spec templates the deliverable lands in
```

## Categories & Skills

### 01-data-exploration-profiling — 5 skills
dataset-first-look · missing-data-strategist · outlier-triage · correlation-radar · distribution-detective

### 02-sql-analytics-engineering — 5 skills
sql-query-forge · query-performance-doctor · data-model-designer · etl-pipeline-blueprint · dbt-transformation-guide

### 03-statistics-experimentation — 5 skills
ab-test-designer · sample-size-power-calculator · causal-inference-advisor · bayesian-analysis-guide · significance-explainer

### 04-machine-learning — 5 skills
ml-problem-framer · model-selection-advisor · feature-engineering-workshop · model-evaluation-auditor · ml-deployment-monitoring-kit

### 05-forecasting-time-series — 5 skills
demand-forecast-builder · seasonality-detector · anomaly-detection-kit · trend-decomposition-analyst · capacity-planning-analyst

### 06-business-analysis — 5 skills
requirements-elicitation-pro · process-mapper-analyst · business-case-builder · kpi-framework-designer · market-swot-competitor-analyst

### 07-finance-risk-analytics — 5 skills
financial-statement-analyzer · budget-variance-analyst · credit-risk-scoring-kit · fraud-pattern-hunter · pricing-optimization-analyst

### 08-customer-product-analytics — 5 skills
customer-segmentation-builder · churn-prediction-retention-kit · clv-ltv-modeler · market-basket-affinity-analyzer · funnel-optimizer

### 09-visualization-storytelling — 5 skills
chart-choice-coach · dashboard-wireframer · executive-narrative-writer · geospatial-insight-builder · survey-sentiment-miner

### 10-data-engineering-modern-stack — 5 skills
api-data-ingestor · web-scraper-compliant · pyspark-bigdata-scaler · cloud-warehouse-cost-optimizer · data-governance-privacy-guardian

### 11-reporting-delivery — 4 skills
| Skill | What it does |
|---|---|
| **report-generator-multiformat** | One Markdown source → styled **HTML**, print-ready **PDF** (weasyprint with browser-print fallback), and clean **Markdown**; includes report design standards + length budgets |
| **interactive-dashboard-builder** | Single-file **interactive HTML dashboards** (Plotly): KPI cards, charts, filters — shareable offline |
| **methodology-explainer** | Explain HOW an analysis was done at three audience depths; write-up + slide formats |
| **master-qa-checklist** | Mandatory pre-delivery gate: master QA checklist, common-error sweep, automated qa_runner, peer review pack, retrospective + learnings log |

## Recommended end-to-end flow
1. **Intake** — requirements-elicitation-pro → signed-off spec
2. **Explore & validate data** — category 01 skills
3. **Build/verify numbers** — categories 02–08 depending on the problem
4. **Visualize** — chart-choice-coach, dashboard-wireframer, or interactive-dashboard-builder
5. **Explain & write** — executive-narrative-writer, methodology-explainer
6. **Generate deliverables** — report-generator-multiformat (MD / HTML / PDF)
7. **QA gate** — master-qa-checklist before anything ships

## Provenance
Category 11 plus many scripts/references/templates across all skills were adapted from the sibling reference library `data-analytics-skills-main` (files suffixed `_src` where a local file already existed). The original reference repo remains untouched for comparison.

## Maintenance
`refresh_skill_resources.py` regenerates the "Execution Protocol" resource map inside every SKILL.md from the actual files present — run it after adding/removing files in any skill folder.
