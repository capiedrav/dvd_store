# pull base image
FROM python:3.6

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# define project directory
WORKDIR /dvd_store

# install dependencies
COPY Pipfile Pipfile.lock /dvd_store/
RUN pip install pipenv && pipenv install --system

# expose default port for Django build-in server
EXPOSE 8000

# copy project files
COPY . .
