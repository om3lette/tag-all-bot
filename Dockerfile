FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
COPY src src

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "-m", "src.main"]
