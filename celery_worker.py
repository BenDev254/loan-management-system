from celery import Celery

def create_celery():
    celery = Celery(
        "tasks",
        broker="redis://localhost:6379/0",
        backend="redis://localhost:6379/0"
    )
    celery.conf.update(task_track_started=True)
    return celery
