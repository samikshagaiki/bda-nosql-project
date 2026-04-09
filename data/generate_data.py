import random
import csv
from datetime import datetime, timedelta

NUM_ROWS = 1_000_000

def random_text():
    words = ["good", "bad", "excellent", "poor", "average", "fast", "slow", "amazing"]
    return " ".join(random.choices(words, k=10))

def random_date():
    start = datetime(2020, 1, 1)
    return start + timedelta(days=random.randint(0, 2000))

with open("reviews.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["review_id","product_id","user_id","rating","review_text","timestamp"])

    for i in range(NUM_ROWS):
        writer.writerow([
            f"R{i}",
            f"P{random.randint(1,1000)}",
            f"U{random.randint(1,5000)}",
            random.randint(1,5),
            random_text(),
            random_date().strftime("%Y-%m-%d")
        ])

        if i % 100000 == 0:
            print(i, "rows done")

print("Dataset ready")