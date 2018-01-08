#!/bin/sh

celery -A celery_tasks worker \
    --loglevel=${WORKER_LOGLEVEL} \
    --concurrency=${WORKER_CONCURRENCY} \
    --purge \
    $*

#    --autoscale=10,2 \
#    -n ${WORKER_NAME} \

# TODO: implment rooting task demo
#-Q ${QUEUE}