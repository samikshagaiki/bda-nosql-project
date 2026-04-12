from db_config import get_collection
import time

collection = get_collection()

# 🔹 1. Get all reviews of a product
def get_reviews(product_id):
    start = time.time()
    data = list(collection.find({"product_id": product_id}, {"_id": 0}))
    end = time.time()

    return len(data), end - start


# 🔹 2. Get reviews by rating
def get_reviews_by_rating(rating):
    start = time.time()
    data = list(collection.find({"rating": rating}, {"_id": 0}))
    end = time.time()

    return len(data), end - start


# 🔹 3. Get low-rated reviews
def get_low_reviews():
    start = time.time()
    data = list(collection.find({"rating": {"$lte": 2}}, {"_id": 0}))
    end = time.time()

    return len(data), end - start


# 🔹 4. Get high-rated reviews
def get_high_reviews():
    start = time.time()
    data = list(collection.find({"rating": {"$gte": 4}}, {"_id": 0}))
    end = time.time()

    return len(data), end - start


# 🔹 5. Get reviews of a user
def get_user_reviews(user_id):
    start = time.time()
    data = list(collection.find({"user_id": user_id}, {"_id": 0}))
    end = time.time()

    return len(data), end - start


# 🔹 6. Get reviews within rating range
def get_rating_range(min_rating, max_rating):
    start = time.time()
    data = list(collection.find({
        "rating": {"$gte": min_rating, "$lte": max_rating}
    }, {"_id": 0}))
    end = time.time()

    return len(data), end - start


# 🔹 MENU (CLI testing)
if __name__ == "__main__":
    print("\nSelect Query Type:")
    print("1. Reviews by Product ID")
    print("2. Reviews by Rating")
    print("3. Low-rated Reviews (≤2)")
    print("4. High-rated Reviews (≥4)")
    print("5. Reviews by User ID")
    print("6. Rating Range")

    choice = input("Enter choice: ")

    if choice == "1":
        pid = input("Enter Product ID: ")
        count, t = get_reviews(pid)

    elif choice == "2":
        rating = int(input("Enter Rating (1–5): "))
        count, t = get_reviews_by_rating(rating)

    elif choice == "3":
        count, t = get_low_reviews()

    elif choice == "4":
        count, t = get_high_reviews()

    elif choice == "5":
        uid = input("Enter User ID: ")
        count, t = get_user_reviews(uid)

    elif choice == "6":
        min_r = int(input("Min Rating: "))
        max_r = int(input("Max Rating: "))
        count, t = get_rating_range(min_r, max_r)

    else:
        print("Invalid choice")
        exit()

    print(f"\nRecords fetched: {count}")
    print(f"Query Time: {t:.4f} seconds")