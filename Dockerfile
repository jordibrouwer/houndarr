# syntax=docker/dockerfile:1
# Houndarr — production Docker image
# Full implementation in Issue #4; this stub satisfies CI scaffolding.
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY VERSION ./

ENV PYTHONPATH=/app/src \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 8877

CMD ["python", "-m", "houndarr", "--help"]
