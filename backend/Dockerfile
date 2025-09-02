FROM python:3.12-slim

# Optionnel mais recommandé : installer dépendances système utiles (certifs, tzdata)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates tzdata && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml /app/

# Installe les deps explicitement (évite le heredoc qui casse le build)
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir \
      fastapi==0.115.0 \
      "uvicorn[standard]==0.30.6" \
      psycopg2-binary==2.9.9 \
      SQLAlchemy==2.0.35 \
      pydantic==2.9.1 \
      httpx==0.27.2 \
      python-dotenv==1.0.1 \
      python-multipart==0.0.9 \
      "pyjwt[crypto]==2.9.0"

COPY app /app/app
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "app.main:create_app", "--host", "0.0.0.0", "--port", "8000"]
