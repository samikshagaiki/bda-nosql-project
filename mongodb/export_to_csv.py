import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
collection = client["productDB"]["reviews"]

# Fetch data (excluding MongoDB _id)
data = list(collection.find({}, {"_id": 0}))

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/exported_reviews.csv", index=False)

print("Data exported to CSV successfully!")