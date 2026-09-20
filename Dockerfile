# Use an older base image so Trivy catches known vulnerabilities
FROM python:3.6-slim

WORKDIR /app

COPY app.py requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
