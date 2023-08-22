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

RUN mkdir -pv /var/log/gunicorn /var/run/gunicorn /var/www/dvd_store/static

# expose port for gunicorn
EXPOSE 8000

# commands to start the container
CMD ["-c", "./project_config/gunicorn.py"]
ENTRYPOINT ["gunicorn"]

# copy project files
COPY . .
