FROM python:3.10-slim-buster
WORKDIR /tz_bot
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
COPY . .
CMD ["python", "src/main.py"]