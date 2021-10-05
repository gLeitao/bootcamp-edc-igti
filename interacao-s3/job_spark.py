from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

enem = (spark.read
            .format("csv")
            .option("header", True)
            .option("inferSchema", True)
            .option("delimiter", ";")
            .load("s3://datalake-geovani-igti/raw-data/enem/")
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-geovani-igti/staging/enem")
)