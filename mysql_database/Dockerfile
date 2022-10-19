# mysql image version
FROM mysql:8.0

# untar database files into container
WORKDIR /database
ADD sakila-db.tar.gz .

# define environment variables
ENV MYSQL_ROOT_PASSWORD="unodostres"
