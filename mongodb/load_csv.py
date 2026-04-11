import pandas as pd
from pymongo import MongoClient
from tqdm import tqdm

client = MongoClient("mongodb://localhost:27017/")
db = client["productDB"]
collection = db["reviews"]

# clear old data (optional)
collection.delete_many({})

chunk_size = 50000

for chunk in tqdm(pd.read_csv("data/reviews.csv", chunksize=chunk_size)):
    records = chunk.to_dict(orient="records")
    collection.insert_many(records)

print("Data successfully loaded into MongoDB!")