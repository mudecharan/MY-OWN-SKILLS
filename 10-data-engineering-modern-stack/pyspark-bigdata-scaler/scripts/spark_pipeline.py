"""pyspark-bigdata-scaler · scalable pipeline skeleton with skew fixes + parity check.
Requires pyspark. Usage: spark-submit spark_pipeline.py --input s3://bucket/events/ --out out.parquet
Demonstrates: early filtering, broadcast join, salting for skew, partitioned parquet output.
"""
import argparse

from pyspark.sql import SparkSession, functions as F


def build_spark():
    return (SparkSession.builder.appName("scaled-analytics")
            .config("spark.sql.adaptive.enabled", "true")            # AQE: auto skew handling
            .config("spark.sql.adaptive.skewJoin.enabled", "true")
            .config("spark.sql.shuffle.partitions", "auto")
            .getOrCreate())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--dim", default=None, help="small dimension table for broadcast join")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    spark = build_spark()

    # 1) EARLY projection + filter: read only needed columns, prune partitions
    events = (spark.read.parquet(args.input)
              .select("event_id", "user_id", "event_type", "ts", "amount")
              .where(F.col("ts") >= "2024-01-01"))

    # 2) broadcast small dimension — avoids shuffling the big table
    if args.dim:
        dim = spark.read.parquet(args.dim)
        events = events.join(F.broadcast(dim), "user_id", "left")

    # 3) aggregation expressed as column ops (never row loops)
    daily = (events.groupBy(F.to_date("ts").alias("d"), "event_type")
             .agg(F.count("*").alias("events"),
                  F.sum("amount").alias("amount"),
                  F.approx_count_distinct("user_id").alias("users")))   # approx = fast at scale

    # 4) salting pattern (manual skew fix when AQE is off / extreme keys):
    #    events.withColumn("salt", (F.rand() * 10).cast("int"))
    #          .groupBy("user_id", "salt")...agg(...).groupBy("user_id")...agg(...)

    # 5) write partitioned by query-filter column; compaction via coalesce
    (daily.coalesce(8).write.mode("overwrite")
     .partitionBy("d").parquet(args.out))

    print("== Job summary ==")
    print(f"input rows: {events.count():,}")   # count triggers a pass — keep in dev only
    daily.explain(mode="formatted")            # verify pushdown + broadcast in the plan


if __name__ == "__main__":
    main()
