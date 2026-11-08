FROM python:3.12-slim

WORKDIR /app

COPY sergiomorais.py .

USER 10001:10001

EXPOSE 8080

CMD ["python", "sergiomorais.py"]
