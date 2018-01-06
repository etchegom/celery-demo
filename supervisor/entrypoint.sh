#!/bin/sh

celery flower -A celery_tasks --port=5555
