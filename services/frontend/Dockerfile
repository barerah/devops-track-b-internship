# Stage 1: Build
   FROM python:3.11-slim AS builder
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Stage 2: Run
   FROM python:3.11-slim
   WORKDIR /app
   
   # Copy only the necessary files from the builder stage
   COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
   COPY --from=builder /usr/local/bin /usr/local/bin
   COPY app.py .

   # Enforce non-root execution (USER 1001)
   RUN useradd -m -u 1001 appuser
   USER 1001

   EXPOSE 8080
   CMD ["python", "app.py"]
