---
name: geospatial-insight-builder
description: Analyze location-based data correctly — joins by geography, choropleth done right, territory analysis, drive-time/isochrone logic, and the ecological fallacy trap. Activate when "where" matters in the data.
---

# When to use
- Store/franchise territory and coverage questions
- Regional performance comparisons on maps
- Delivery/logistics catchment analysis

# Process
1. **Geocode & validate** — convert addresses to coordinates; measure match rate; unmatched records are a silent bias — quantify before analyzing.
2. **Spatial join discipline** — point-in-polygon assignment; beware boundary effects and mismatched geography levels (customers in postcodes vs stores in districts).
3. **Choropleth done right** — normalize by exposure (revenue per capita, not raw revenue — bigger regions always win raw maps); sensible classification breaks (quantiles/jenks, never rainbow); consider cartograms when region size misleads.
4. **Distance analytics** — haversine for straight-line, OSRM/Google for drive-time; isochrone catchments for coverage questions ("who can reach a store in 15 min?").
5. **Spatial patterns** — hotspot detection (Getis-Ord), spatial autocorrelation (Moran's I) before claiming clusters; adjacency-aware comparisons.
6. **Fallacy guard** — area-level findings ≠ individual-level conclusions (ecological fallacy); state the analysis unit explicitly.

# Inputs the skill needs
- Required: location data (addresses/coords/regions), boundary files
- Optional: road network access for isochrones, demographic denominators

# Output
- Validated geocoded dataset with match-rate report
- Normalized maps with defensible classifications
- Spatial findings: hotspots, coverage gaps, territory recommendations

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/geo_analysis.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/spatial_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/findings_template.md` - Fill this template - it IS the deliverable format.
