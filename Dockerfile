FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
EXPOSE 8000

RUN python -m pip install --upgrade pip

COPY . /code/