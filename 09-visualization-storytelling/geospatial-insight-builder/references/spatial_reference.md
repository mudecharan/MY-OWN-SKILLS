# Spatial Analysis Reference

## Geocoding quality gate (before ANY analysis)
- Match rate reported; unmatched records are a silent bias — are failures
  systematic (rural? certain cities?) or random?
- Default-coordinate artifacts: many records at the exact centroid of a city
  = lazy geocoding; cluster-count check catches this.

## Choropleth rules (the most-abused map)
| Rule | Why |
|---|---|
| Normalize by exposure (per capita / per household / per visit) | raw counts always light up the biggest/most populous areas |
| Quantile or Jenks classification, 5–7 bins | rainbow + equal intervals hide patterns |
| Consider cartograms when region SIZE misleads | big empty areas dominate visually |
| State the analysis unit | area-level findings ≠ individual conclusions |

## Distance & catchments
- haversine = straight line; drive-time is what customers experience → OSRM/Google.
- Isochrone catchments ("who can reach a store within 15 min") answer coverage questions
  that radius circles answer wrongly.

## Spatial statistics before claiming clusters
- Global Moran's I: is there clustering at all beyond chance?
- Getis-Ord Gi*: WHERE are the significant hot/cold spots?
- Adjacent regions aren't independent — spatial autocorrelation inflates naive significance.

## Ecological fallacy guard
High-revenue regions ≠ high-revenue people in them. Keep unit of analysis explicit
in every sentence of the writeup.
