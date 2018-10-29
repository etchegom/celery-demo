# coding=utf-8

import os
import time
import logging
from celery_tasks import add, multiply
from random import randint

log = logging.getLogger('stresser')


def start_add_task():
    task = add.apply_async(kwargs={'x': randint(0, 9), 'y': randint(0, 9)}, retry=False)
    log.info('new task "add" %s' % task.id)


def start_multiply_task():
    task = multiply.apply_async(kwargs={'x': randint(0, 9), 'y': randint(0, 9)}, retry=False)
    log.info('new task "multiply" %s' % task.id)


if __name__ == '__main__':
    logging.basicConfig(level='INFO', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    timer = int(os.getenv('TIMER', '100')) / 1000
    while True:
        start_add_task()
        start_multiply_task()
        time.sleep(timer)
