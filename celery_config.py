from celery import Celery

celery = Celery(
    'tasks',
    broker='pyamqp://guest@localhost//',
    backend='rpc://'
)
celery.conf.update(
    task_routes={
        'app.tasks.send_email': {'queue': 'emails'},
        'app.tasks.log_time': {'queue': 'logs'},
    }
)
