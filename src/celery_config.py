# coding=utf-8

"""
Celery configuration
"""

broker_url = 'redis://broker:6379/0'
result_backend = 'redis://broker:6379/1'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

task_track_started = True

task_soft_time_limit = 300
task_time_limit = 600
task_ignore_result = True

timezone = 'Europe/Paris'
enable_utc = True
