from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Review Analysis") \
    .getOrCreate()

df = spark.read.csv("data/reviews.csv", header=True, inferSchema=True)

df.printSchema()

# Average rating
df.groupBy("product_id").avg("rating").show()

# Count reviews
df.groupBy("product_id").count().show()

# Top products
df.groupBy("product_id") \
  .avg("rating") \
  .orderBy("avg(rating)", ascending=False) \
  .show(10)