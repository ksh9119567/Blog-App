# =========================
#   FastAPI App Container
# =========================

# 1️⃣ Use a lightweight Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Install required system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# 4️⃣ Copy requirement file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy the entire app into container
COPY . .

# 6️⃣ Copy and prepare startup script
RUN chmod +x scripts/wait_for_db.sh

# 7️⃣ Expose FastAPI port
EXPOSE 8000

# 8️⃣ Run Alembic migrations and start FastAPI
CMD ["bash", "-c", "./wait_for_db.sh db alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
