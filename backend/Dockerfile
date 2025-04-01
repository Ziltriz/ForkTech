FROM python:3.11-slim AS base

WORKDIR /app

FROM base AS development

RUN pip install --no-cache-dir "uvicorn[standard]" alembic watchdog

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

FROM base AS production

ENV PYTHONPATH="${PYTHONPATH}:/app"

COPY . .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--reload"]