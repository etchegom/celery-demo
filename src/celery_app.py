# coding=utf-8

from celery import Celery


def add_worker_arguments(parser):
    parser.add_argument(
        '--extra-option', dest='extra_option', help='My worker extra option',
    )


app = Celery()
app.config_from_object('celery_config')
app.user_options['worker'].add(add_worker_arguments)
