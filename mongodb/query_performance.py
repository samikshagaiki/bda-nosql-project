from pymongo import MongoClient
import time

client = MongoClient("mongodb://localhost:27017/")
collection = client["productDB"]["reviews"]

# Query BEFORE index (run before creating index)
start = time.time()
data = list(collection.find({"product_id": "P10"}))

end = time.time()

print(f"Records fetched: {len(data)}")
print("Query Time:", end - start)

# ---- NEW AGGREGATION PIPELINE ----
print("\nTop 5 products by number of reviews:\n")

pipeline = [
    {"$group": {"_id": "$product_id", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 5}
]

for doc in collection.aggregate(pipeline):
    print(doc)