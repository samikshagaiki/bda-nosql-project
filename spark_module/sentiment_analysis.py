from spark_module.spark_session import get_spark
from pyspark.sql.functions import when

spark = get_spark()

def load_data(path="data/reviews.csv"):
    return spark.read.csv(path, header=True, inferSchema=True)


def sentiment(df):
    df = df.withColumn(
        "sentiment",
        when(df.rating >= 4, "Positive")
        .when(df.rating <= 2, "Negative")
        .otherwise("Neutral")
    )
    return df.groupBy("sentiment").count()


if __name__ == "__main__":
    df = load_data()
    sentiment(df).show()