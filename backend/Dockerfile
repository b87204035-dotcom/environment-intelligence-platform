FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN addgroup --system eip && adduser --system --ingroup eip eip
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --no-cache-dir .
COPY alembic.ini ./
COPY alembic ./alembic
COPY app ./app
RUN mkdir -p /data/snapshots && chown -R eip:eip /app /data
USER eip
EXPOSE 8000
CMD ["sh","-c","alembic upgrade head && exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --proxy-headers"]
