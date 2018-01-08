# coding=utf-8

"""
Celery configuration
"""

from kombu import Exchange, Queue

broker_url = 'redis://broker:6379/0'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

task_track_started = True

task_soft_time_limit = 300
task_time_limit = 600

# results are ignored on this demo
# result_backend = 'redis://broker:6379/1'
task_ignore_result = True

timezone = 'Europe/Paris'
enable_utc = True


# TODO: implement routing example

# default_exchange = Exchange('default', type='direct')
# media_exchange = Exchange('media', type='direct')
#
# task_default_queue = 'default'
# task_default_exchange_type = 'direct'
# task_default_routing_key = 'default'
#
# task_queues = (
#     Queue('default', Exchange('default'), routing_key='default'),
#     Queue('videos',  Exchange('media'),   routing_key='media.video'),
#     Queue('images',  Exchange('media'),   routing_key='media.image'),
# )
# CELERY_QUEUES = (
#     Queue('media', [
#         binding(media_exchange, routing_key='media.video'),
#         binding(media_exchange, routing_key='media.image'),
#     ]),
# )
#
# task_routes = {
#     'celery.ping': 'default',
#     'celery_tasks.add': 'cpu-bound',
#     'video.encode': {
#         'queue': 'video',
#         'exchange': 'media'
#         'routing_key': 'media.video.encode',
#     },
# }

