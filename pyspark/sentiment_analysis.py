from pyspark.sql import SparkSession
from pyspark.sql.functions import when

spark = SparkSession.builder.appName("Sentiment").getOrCreate()

df = spark.read.csv("data/reviews.csv", header=True, inferSchema=True)

df = df.withColumn(
    "sentiment",
    when(df.rating >= 4, "Positive")
    .when(df.rating <= 2, "Negative")
    .otherwise("Neutral")
)

df.groupBy("sentiment").count().show()