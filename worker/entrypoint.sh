#!/bin/sh

celery -A celery_tasks worker \
    --loglevel=${WORKER_LOGLEVEL} \
    --autoscale=10,2 \
    --purge \
    $*

#    -n ${WORKER_NAME} \
#    --concurrency=${WORKER_CONCURRENCY} \
