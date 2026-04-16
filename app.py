import streamlit as st
import time
import pandas as pd
from mongodb.db_config import get_collection
from spark_module.spark_analysis import load_data, avg_rating, review_count, top_products
from spark_module.sentiment_analysis import sentiment

collection = get_collection()

st.title("🛍️ Product Review Analyzer Dashboard")

# Sidebar
menu = st.sidebar.selectbox(
    "Select Section",
    ["Query Explorer", "Index Performance", "Analytics Dashboard"]
)

# ---------------------------------------------------
# 🔹 1. QUERY EXPLORER
# ---------------------------------------------------

if menu == "Query Explorer":

    st.header("🔍 MongoDB Query Explorer")

    query_type = st.selectbox(
        "Select Query Type",
        [
            "Product Reviews",
            "Rating Filter",
            "User Reviews",
            "Low Rated",
            "High Rated"
        ]
    )

    def display_results(data, start, end):
        df = pd.DataFrame(data)
        st.write(f"Records: {len(df)}")
        st.write(f"Time: {end - start:.4f} sec")

        if not df.empty:
            st.dataframe(df.head(20))
            st.download_button("Download CSV", df.to_csv(index=False), "data.csv")
        else:
            st.warning("No data found")

    # ---------------------

    if query_type == "Product Reviews":
        pid = st.text_input("Enter Product ID")

        if st.button("Run Query"):
            start = time.time()
            data = list(collection.find({"product_id": pid}, {"_id": 0}))
            end = time.time()
            display_results(data, start, end)

    # ---------------------

    elif query_type == "Rating Filter":
        rating = st.slider("Rating", 1, 5)

        if st.button("Run Query"):
            start = time.time()
            data = list(collection.find({"rating": rating}, {"_id": 0}))
            end = time.time()
            display_results(data, start, end)

    # ---------------------

    elif query_type == "User Reviews":
        uid = st.text_input("Enter User ID")

        if st.button("Run Query"):
            start = time.time()
            data = list(collection.find({"user_id": uid}, {"_id": 0}))
            end = time.time()
            display_results(data, start, end)

    # ---------------------

    elif query_type == "Low Rated":
        if st.button("Run Query"):
            start = time.time()
            data = list(collection.find({"rating": {"$lte": 2}}, {"_id": 0}))
            end = time.time()
            display_results(data, start, end)

    # ---------------------

    elif query_type == "High Rated":
        if st.button("Run Query"):
            start = time.time()
            data = list(collection.find({"rating": {"$gte": 4}}, {"_id": 0}))
            end = time.time()
            display_results(data, start, end)


# ---------------------------------------------------
# 🔹 2. INDEX PERFORMANCE
# ---------------------------------------------------

elif menu == "Index Performance":

    st.header("⚡ Indexing Performance Comparison")

    pid = st.text_input("Enter Product ID for Testing")

    if st.button("Compare Performance"):

        if not pid:
            st.warning("Please enter a Product ID")
        else:
            st.write("Running comparison...")

            # Drop existing indexes except _id
            indexes = collection.index_information()
            for index in indexes:
                if index != "_id_":
                    collection.drop_index(index)

            # Without index
            start1 = time.time()
            list(collection.find({"product_id": pid}))
            end1 = time.time()
            time_without_index = end1 - start1

            # Create index
            collection.create_index([("product_id", 1)])

            # With index
            start2 = time.time()
            list(collection.find({"product_id": pid}))
            end2 = time.time()
            time_with_index = end2 - start2

            # Result table
            df = pd.DataFrame({
                "Scenario": ["Without Index", "With Index"],
                "Time (sec)": [time_without_index, time_with_index]
            })

            st.subheader("Performance Comparison")
            st.dataframe(df)
            st.bar_chart(df.set_index("Scenario"))


# ---------------------------------------------------
# 🔹 3. ANALYTICS DASHBOARD
# ---------------------------------------------------

elif menu == "Analytics Dashboard":

    st.header("📊 Big Data Analytics (PySpark)")

    if st.button("Run Analysis"):

        with st.spinner("Running PySpark Analysis..."):

            df = load_data()

            st.subheader("Average Rating per Product")
            avg_df = avg_rating(df).toPandas()
            st.dataframe(avg_df.head(20))

            st.subheader("Review Count")
            count_df = review_count(df).toPandas()
            st.dataframe(count_df.head(20))

            st.subheader("Top Products")
            top_df = top_products(df).toPandas()
            st.dataframe(top_df)

            st.bar_chart(top_df.set_index("product_id"))

    # ---------------------

    st.subheader("Sentiment Analysis")

    if st.button("Run Sentiment"):

        with st.spinner("Running Sentiment Analysis..."):

            df = load_data()
            sent_df = sentiment(df).toPandas()

            st.dataframe(sent_df)
            st.bar_chart(sent_df.set_index("sentiment"))