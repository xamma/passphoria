FROM python:3.13-slim AS builder

WORKDIR /app

COPY src/requirements.txt /opt/requirements.txt

RUN pip install --no-cache-dir --target=/app -r /opt/requirements.txt

COPY src/main /app

FROM gcr.io/distroless/python3-debian12

COPY --from=builder /app /app

WORKDIR /app

ENV PYTHONPATH /app

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]