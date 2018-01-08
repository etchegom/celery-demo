# coding=utf-8


import time
import logging
from celery_tasks import add
from random import randint

log = logging.getLogger('stresser')


def start_simple_task():
    task = add.apply_async(kwargs={'x': randint(0, 9), 'y': randint(0, 9)}, retry=False)
    log.info('new task %s' % task.id)


if __name__ == '__main__':
    logging.basicConfig(level='INFO', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    while True:
        start_simple_task()
        # TODO: put timer value in args  so that we can play from docker launching
        time.sleep(0.1)
