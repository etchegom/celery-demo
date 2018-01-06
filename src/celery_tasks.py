# coding=utf-8

from celery_app import app
from celery.exceptions import SoftTimeLimitExceeded
from celery.task import Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def add(x, y):
    return x + y


class MyTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass


@app.task
def my_task(base=MyTask):
    try:
        logger.info("task")
    except SoftTimeLimitExceeded:
        pass
