FROM python:3.9.15

RUN pip install -U pip && pip install numpy && pip install matplotlib
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y cron
WORKDIR /runner
COPY src/ src/
RUN chmod +x src/imager.py

RUN { \
        echo "SHELL=/bin/bash"; \
        echo "TZ=Asia/Tokyo"; \
        echo "*  *  *  *  * /runner/src/imager.py >> /var/log/rtt.log 2>&1"; \
} > /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab -u root /etc/cron.d/cronjob

CMD ["cron", "-f"]