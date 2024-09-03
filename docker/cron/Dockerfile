FROM php:8.2-cli

RUN apt-get update && apt-get install -y cron supervisor

COPY ./docker/cron/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./docker/cron/crontab /etc/cron.d/symfony-cron

RUN chmod 0644 /etc/cron.d/symfony-cron

# Add this line to print the contents of the crontab file
RUN cat /etc/cron.d/symfony-cron

RUN crontab /etc/cron.d/symfony-cron

CMD ["/usr/bin/supervisord"]