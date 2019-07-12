FROM python:2.7.11

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

