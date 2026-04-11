from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
collection = client["productDB"]["reviews"]

query = {
    "product_id": "P10",
    "rating": 5
}

cursor = collection.find(query, {"_id": 0})

with open("data/p10_reviews.json", "w", encoding="utf-8") as f:
    f.write("[\n")
    for i, doc in enumerate(cursor):
        if i > 0:
            f.write(",\n")
        json.dump(doc, f)
    f.write("\n]")

print("Filtered data exported!")