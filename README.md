## CELERY demo

Implements a stack made of the following componants:
* a redis broker
* a celery worker (scalable)
* a stresser script
* a monitoring tool

Celery documentation is here:
http://docs.celeryproject.org/en/latest/index.html


#### How to

Run the full stack
```
docker-compose up -d --build
```

Check results through the monitoring view:
http://localhost:5555


Add new workers so that tasks number decrease
```
docker-compose scale worker=5
```