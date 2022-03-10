from celery import Celery

task = Celery('tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

task.conf.timezone = 'UTC'

'''
@task.task
def function():
    ... 
'''
@task.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, periodic_task.s(), name='clean every 10s')

@task.task
def periodic_task():
    pass