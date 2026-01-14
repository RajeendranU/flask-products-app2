# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app.py
COPY app.py .

# Expose port 5002
EXPOSE 5002

# Run gunicorn with 4 workers on port 5002
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5002", "app:app"]
