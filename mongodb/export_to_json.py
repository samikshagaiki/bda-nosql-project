from mongodb.db_config import get_collection
import json

collection = get_collection()

def export_json(product_id):
    data = list(collection.find({"product_id": product_id}, {"_id": 0}))

    filename = f"data/{product_id}_reviews.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

    return filename


if __name__ == "__main__":
    product_id = input("Enter Product ID: ")
    file = export_json(product_id)
    print(f"Exported to {file}")