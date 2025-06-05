FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set environment variables for Airflow
ENV AIRFLOW_VERSION=2.7.3 \
    PYTHON_VERSION=3.10

# Install system dependencies for Airflow + psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean

# Copy application files
COPY . .

# Upgrade pip and install Airflow constraints file
RUN pip install --upgrade pip setuptools wheel && \
    curl -sSL "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt" -o constraints.txt

# Install Flask + Airflow + other deps using the constraint file
RUN pip install -r requirements.txt --constraint constraints.txt

# Set Flask environment variables
ENV FLASK_APP=api/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose Flask default port
EXPOSE 5000

# Run Flask app
CMD ["flask", "run"]
