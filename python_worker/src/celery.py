from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@rabbitmq//')

app.conf.update(
    result_backend='rpc://',
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

@app.task
def add(x, y):
    return x + y