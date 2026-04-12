FROM python:3.9-slim

# Install Java (correct package)
RUN apt-get update && apt-get install -y default-jdk

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/default-java

# Install PySpark
RUN pip install --no-cache-dir pyspark pandas

WORKDIR /app

COPY . .

CMD ["python", "pyspark/spark_analysis.py"]