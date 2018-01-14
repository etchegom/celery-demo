#!/bin/sh

celery -A celery_tasks worker \
    --loglevel=${WORKER_LOGLEVEL} \
    --concurrency=${WORKER_CONCURRENCY} \
    -Q ${WORKER_QUEUE}
    $*

#    --autoscale=10,2 \
#    -n ${WORKER_NAME} \
