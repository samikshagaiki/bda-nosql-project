# Product Review Storage and Retrieval using NoSQL

## Project Overview
This project demonstrates handling large-scale product review data using NoSQL and performing analytics using PySpark.

We simulate a real-world big data system where millions of user reviews are stored, retrieved, and analyzed efficiently.

---

## Objectives
- Store large-scale unstructured data using MongoDB
- Perform fast retrieval using indexing
- Analyze big data using PySpark
- Containerize the entire system using Docker

---

## Dataset
- Generated dataset of 1 million product reviews
- Fields:
  - review_id
  - product_id
  - user_id
  - rating (1–5)
  - review_text
  - timestamp

---

## Project Structure

bda-nosql-project/
│
├── data/
│   └── reviews.csv
│
├── mongodb/
│   ├── load_data.py
│   ├── create_indexes.py
│   ├── query_reviews.py
│
├── pyspark/
│   ├── spark_analysis.py
│   ├── sentiment_analysis.py
│
├── Dockerfile
├── README.md

---

## Technologies Used
- MongoDB (NoSQL Database)
- PySpark (Big Data Processing)
- Docker (Containerization)
- Python

---

## Features

### MongoDB
- Stores large-scale review data
- Uses indexing for faster query execution

### PySpark Analytics
- Computes average rating per product
- Counts number of reviews per product
- Identifies top-rated products

### Sentiment Analysis
- Positive (rating ≥ 4)
- Neutral (rating = 3)
- Negative (rating ≤ 2)

### Docker Integration
- Ensures portability and consistency
- Eliminates dependency issues

---

## How to Run the Project

Step 1: Build Docker Image
docker build -t pyspark-bda .

Step 2: Run PySpark Analysis
docker run -it --rm pyspark-bda

Step 3: Run Sentiment Analysis
docker run -it --rm pyspark-bda python pyspark/sentiment_analysis.py

---

## Key Concepts Covered
- NoSQL Databases
- Indexing
- Scalability
- Distributed Computing (PySpark)
- Containerization (Docker)

---

## Conclusion
This project demonstrates:
- Efficient storage and retrieval of large-scale data using MongoDB
- Scalable data processing using PySpark
- Portable deployment using Docker

---

## Contributors
- Add team member names here

---

## Future Improvements
- Real-time data streaming using Kafka
- Advanced sentiment analysis using NLP
- Dashboard visualization
