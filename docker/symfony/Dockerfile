FROM php:8.2-fpm-alpine

RUN apk add --no-cache $PHPIZE_DEPS \
    && pecl install redis \
    && docker-php-ext-enable redis \
    && apk add --no-cache rabbitmq-c-dev \
    && pecl install amqp \
    && docker-php-ext-enable amqp \
    && apk add --no-cache postgresql-dev \
    && docker-php-ext-install pdo pdo_pgsql \
    && apk add --no-cache bash

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

RUN wget https://get.symfony.com/cli/installer -O - | bash \
    && mv /root/.symfony5/bin/symfony /usr/local/bin/symfony

WORKDIR /var/www/symfony

COPY symfony/ .

COPY docker/symfony/php.ini /usr/local/etc/php/conf.d/app.ini

RUN composer install

RUN chown -R www-data:www-data var