#!/bin/sh

celery -A celery_tasks worker \
    --loglevel=${WORKER_LOGLEVEL} \
    --concurrency=${WORKER_CONCURRENCY} \
    -Q ${WORKER_QUEUE} \
    --extra-option ${WORKER_EXTRA_OPTION} \
    $*
