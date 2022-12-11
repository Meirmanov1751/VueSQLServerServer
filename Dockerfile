FROM python:3

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY . /app
RUN pip install -r requirments.txt

