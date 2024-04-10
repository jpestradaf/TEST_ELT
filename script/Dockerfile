FROM python:3.8-slim

RUN apt-get update && apt-get install -y postgresql-client cron

COPY run.sh /app/run.sh

COPY elt.py .

WORKDIR /app

RUN echo "0 6 * * * python /app/elt.py" | crontab -

CMD ["python", "elt.py"]