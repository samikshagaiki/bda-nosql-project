from mongodb.db_config import get_collection
import pandas as pd

collection = get_collection()

def export_csv(product_id):
    data = list(collection.find({"product_id": product_id}, {"_id": 0}))
    df = pd.DataFrame(data)

    filename = f"data/{product_id}_reviews.csv"
    df.to_csv(filename, index=False)

    return filename


if __name__ == "__main__":
    product_id = input("Enter Product ID: ")
    file = export_csv(product_id)
    print(f"Exported to {file}")