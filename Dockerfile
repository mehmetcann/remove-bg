FROM python:3.9-slim

# Install system dependencies for image processing
RUN apt-get update && apt-get install -y libgl1 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
