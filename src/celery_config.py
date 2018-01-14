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

task_default_queue = 'default'
task_queues = (
    Queue('queue1', routing_key='queue1'),
    Queue('queue2', routing_key='queue1'),
)

task_routes = {
    'celery_tasks.add': {
        'queue': 'queue1',
        'routing_key': 'queue1'
    },
    'celery_tasks.multiply': {
        'queue': 'queue2',
        'routing_key': 'queue1'
    }
}
