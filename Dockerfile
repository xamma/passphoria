FROM python:3.13-slim

WORKDIR /app

COPY src/requirements.txt /opt/requirements.txt

RUN pip install --no-cache-dir -r /opt/requirements.txt

COPY src/main /app

RUN adduser --system appuser

USER appuser

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]