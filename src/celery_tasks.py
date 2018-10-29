# coding=utf-8

from celery.signals import celeryd_init
from celery.utils.log import get_task_logger

from celery_app import app

logger = get_task_logger(__name__)


class Extra:
    def __init__(self):
        self.option = None

    def init(self, option):
        self.option = option


extra = Extra()


@celeryd_init.connect()
def configure_workers(options, **kwargs):
    extra.init(options.get('extra_option', None))


@app.task
def add(x, y):
    logger.info("extra option is %s" % extra.option)
    return x + y


@app.task
def multiply(x, y):
    logger.info("extra option is %s" % extra.option)
    return x * y
