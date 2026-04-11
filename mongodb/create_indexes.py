from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
collection = client["productDB"]["reviews"]

collection.create_index("product_id")
collection.create_index("rating")
collection.create_index("user_id")

print("Indexes created successfully!")