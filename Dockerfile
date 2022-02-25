FROM python:3.9.0b4-alpine3.12
COPY wwwroot /bin/wwwroot
COPY py_file /bin/py_file
COPY crontab /var/spool/cron/crontabs/root
RUN chmod +x /bin/py_file
CMD crond -l 2 -f
