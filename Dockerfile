# Dockerfile

FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system

COPY . /code/
