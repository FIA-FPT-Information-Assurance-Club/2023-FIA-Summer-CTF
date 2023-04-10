# Use the official PHP 7.2 Apache image
#FROM ubuntu:16.04
FROM php:7.2-apache

#RUN apt-get update && apt-get -y install software-properties-common && add-apt-repository ppa:ondrej/php && apt-get update && apt-get install -y apache2 && apt-get install -y php7.2 && apt-get install -y libapache2-mod-php7.2 php7.2-curl php7.2-json && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html/
COPY ./src .

# Configure permissions and ownership for the application code
RUN chown -R root:www-data .
RUN chmod 750 .
RUN find . -type f -exec chmod 640 {} \;
RUN find . -type d -exec chmod 750 {} \;

# Set the sticky bit to prevent deletion of files and directories
RUN chmod +t -R .