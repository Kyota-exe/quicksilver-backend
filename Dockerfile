FROM python:3.12-slim

# Don't write .pyc files (less clutter)
ENV PYTHONDONTWRITEBYTECODE=1

# Real-time logs (no stdout/stderr buffering)
ENV PYTHONUNBUFFERED=1

# Installs tooling that is needed during `pip install` for some packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && gunicorn backend.wsgi:application --bind 0.0.0.0:8000"]

