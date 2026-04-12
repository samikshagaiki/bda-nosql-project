import streamlit as st
from mongodb.query_performance import (
    get_reviews,
    get_reviews_by_rating,
    get_low_reviews,
    get_high_reviews,
    get_user_reviews,
    get_rating_range
)
# from pyspark.spark_analysis import load_data, avg_rating, review_count, top_products
# from pyspark.sentiment_analysis import sentiment

# Page title
st.title("🛍️ Product Review Analyzer Dashboard")

# Sidebar
st.sidebar.header("Choose Operation")

option = st.sidebar.selectbox(
    "Select Function",
    [
        "Product Reviews",
        "Rating Filter",
        "Low Rated Reviews",
        "High Rated Reviews",
        "User Reviews",
        "Rating Range"
    ]
)

# -------------------------------
# MongoDB Queries
# -------------------------------

if option == "Product Reviews":
    pid = st.text_input("Enter Product ID (e.g., P10)")

    if st.button("Fetch Reviews"):
        count, t = get_reviews(pid)
        st.write(f"Total Reviews: {count}")
        st.write(f"Query Time: {t:.4f} sec")

# -------------------------------

elif option == "Rating Filter":
    rating = st.slider("Select Rating", 1, 5)

    if st.button("Fetch"):
        count, t = get_reviews_by_rating(rating)
        st.write(f"Reviews Found: {count}")
        st.write(f"Query Time: {t:.4f} sec")

# -------------------------------

elif option == "Low Rated Reviews":
    if st.button("Fetch"):
        count, t = get_low_reviews()
        st.write(f"Low Reviews: {count}")
        st.write(f"Query Time: {t:.4f} sec")

# -------------------------------

elif option == "High Rated Reviews":
    if st.button("Fetch"):
        count, t = get_high_reviews()
        st.write(f"High Reviews: {count}")
        st.write(f"Query Time: {t:.4f} sec")

# -------------------------------

elif option == "User Reviews":
    uid = st.text_input("Enter User ID (e.g., U10)")

    if st.button("Fetch"):
        count, t = get_user_reviews(uid)
        st.write(f"User Reviews: {count}")
        st.write(f"Query Time: {t:.4f} sec")

# -------------------------------

elif option == "Rating Range":
    min_r = st.slider("Min Rating", 1, 5)
    max_r = st.slider("Max Rating", 1, 5)

    if st.button("Fetch"):
        count, t = get_rating_range(min_r, max_r)
        st.write(f"Reviews: {count}")
        st.write(f"Query Time: {t:.4f} sec")

# -------------------------------
# PySpark Analytics
# -------------------------------

# elif option == "Analytics (PySpark)":
#     if st.button("Run Analysis"):
#         df = load_data()

#         st.subheader("Average Ratings")
#         st.dataframe(avg_rating(df).toPandas())

#         st.subheader("Review Count")
#         st.dataframe(review_count(df).toPandas())

#         st.subheader("Top Products")
#         st.dataframe(top_products(df).toPandas())

# -------------------------------
# Sentiment Analysis
# -------------------------------

# elif option == "Sentiment Analysis":
#     if st.button("Run Sentiment"):
#         df = load_data()
#         result = sentiment(df).toPandas()

#         st.subheader("Sentiment Distribution")
#         st.dataframe(result)

#         st.bar_chart(result.set_index("sentiment"))