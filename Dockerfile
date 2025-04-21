FROM python:3.12-slim

WORKDIR /tag-all-bot

COPY src src
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "-m", "src.main"]
