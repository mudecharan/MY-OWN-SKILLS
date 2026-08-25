"""geospatial-insight-builder · geocoding validation, normalized choropleth, hotspot stats.
Usage: python geo_analysis.py --points points.csv --lat_col lat --lon_col lon [--regions regions.geojson --metric revenue]
points.csv needs lat/lon. regions.geojson optional for choropleth normalization.
"""
import argparse

import numpy as np
import pandas as pd


def haversine(lat1, lon1, lat2, lon2):
    r = 6371
    p1, p2 = np.radians(lat1), np.radians(lat2)
    dp, dl = np.radians(lat2 - lat1), np.radians(lon2 - lon1)
    a = np.sin(dp/2)**2 + np.cos(p1) * np.cos(p2) * np.sin(dl/2)**2
    return 2 * r * np.arcsin(np.sqrt(a))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--points", required=True)
    ap.add_argument("--lat-col", default="lat")
    ap.add_argument("--lon-col", default="lon")
    ap.add_argument("--regions", default=None, help="geojson for choropleth")
    ap.add_argument("--metric", default=None, help="column to normalize per region")
    ap.add_argument("--plot", default="map.png")
    args = ap.parse_args()

    df = pd.read_csv(args.points)
    lat, lon = df[args.lat_col], df[args.lon_col]

    # --- validity & geocoding quality ---
    valid = lat.between(-90, 90) & lon.between(-180, 180) & lat.notna() & lon.notna()
    print(f"Geocode validity: {valid.mean():.1%} valid coordinates")
    if valid.mean() < 0.95:
        print("⚠ >5% invalid/unmatched — quantify the bias before analyzing "
              "(which records failed to geocode? systematic by region?)")
    # duplicate exact coordinates = default-city centroid artifacts
    dupes = df[valid].groupby([lat[valid].round(4), lon[valid].round(4)]).size()
    print(f"Exact-coordinate clusters (possible default geocodes): {(dupes > 10).sum()}")

    # --- distance stats ---
    d = haversine(lat[valid].values, lon[valid].values,
                  lat[valid].shift().fillna(lat[valid]).values,
                  lon[valid].shift().fillna(lon[valid]).values)
    print(f"Consecutive point distances: median={np.median(d[1:]):.1f} km")

    # --- choropleth with NORMALIZATION warning ---
    if args.regions and args.metric:
        import geopandas as gpd
        gdf = gpd.read_file(args.regions)
        joined = gpd.sjoin(gdf, gpd.GeoDataFrame(
            df[valid], geometry=gpd.points_from_xy(lon[valid], lat[valid]), crs=gdf.crs),
            how="left")
        agg = joined.groupby(joined.index.names[0])[args.metric].sum()
        gdf["raw"] = gdf.index.map(agg).fillna(0)
        if "population" in gdf.columns:   # exposure denominator
            gdf["normalized"] = gdf["raw"] / gdf["population"]
        print("\n⚠ RAW counts on a choropleth always light up the biggest regions. "
              "Normalize by exposure (population, traffic, households).")

    fig, ax = plt.subplots(figsize=(8, 8)) if False else (None, None)
    try:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.scatter(lon[valid], lat[valid], s=6, alpha=.4, c="#4a9eed")
        ax.set_title("points (validate against known geography!)")
        fig.savefig(args.plot, dpi=130)
        print(f"plot -> {args.plot}")
    except Exception as e:
        print(f"(plot skipped: {e})")


if __name__ == "__main__":
    main()
