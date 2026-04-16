from spark_module.spark_session import get_spark

spark = get_spark()

def load_data(path="data/reviews.csv"):
    return spark.read.csv(path, header=True, inferSchema=True)


def avg_rating(df):
    return df.groupBy("product_id").avg("rating")


def review_count(df):
    return df.groupBy("product_id").count()


def top_products(df, n=10):
    return df.groupBy("product_id") \
        .avg("rating") \
        .orderBy("avg(rating)", ascending=False) \
        .limit(n)


if __name__ == "__main__":
    df = load_data()

    print("\nAverage Ratings:")
    avg_rating(df).show()

    print("\nReview Count:")
    review_count(df).show()

    print("\nTop Products:")
    top_products(df).show()