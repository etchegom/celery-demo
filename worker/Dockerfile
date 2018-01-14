FROM python:3-alpine

RUN mkdir /app
VOLUME /app

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt && rm -f /requirements.txt

ENV WORKER_CONCURRENCY=1
ENV WORKER_LOGLEVEL=info
ENV WORKER_NAME=worker
ENV WORKER_QUEUE=queue

COPY ./entrypoint.sh /

WORKDIR /app
CMD ["/entrypoint.sh"]
