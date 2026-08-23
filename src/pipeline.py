from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("CustomerPipeline")
    .getOrCreate()
)

# Lectura
df = spark.read.csv(
    "data/raw/customer_churn.csv",
    header=True,
    inferSchema=True
)

# Validaciones
total_rows = df.count()
distinct_rows = df.distinct().count()

print(f"Rows: {total_rows}")
print(f"Distinct Rows: {distinct_rows}")
print(f"Columns: {len(df.columns)}")

# Transformaciones de negocio
df_final = (
    df
    .withColumn(
        "churn_desc",
        F.when(F.col("churn") == 1, "Churned")
        .otherwise("Active")
    )
    .withColumn(
        "age_group",
        F.when(F.col("age") < 30, "Young")
        .when(F.col("age") < 50, "Adult")
        .otherwise("Senior")
    )
)

# Validación final
df_final.groupBy(
    "age_group",
    "churn_desc"
).count().show()

# Exportación
df_final.toPandas().to_parquet(
    "data/curated/customer_churn.parquet",
    index=False
)

print(f"Rows: {total_rows}")
print(f"Distinct Rows: {distinct_rows}")
print(f"Columns: {len(df.columns)}")

print("\nNull Validation")

df.select(
    *[
        F.count(
            F.when(F.col(c).isNull(), c)
        ).alias(c)
        for c in df.columns
    ]
).show()

spark.stop()