from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery import current_app
from celery.bin import worker

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sportsroom.settings')
app = Celery('sportsroom')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


if __name__ == '__main__':
    worker = worker.worker(app=app)

    options = {
        'broker': 'amqp://guest:guest@localhost:5672//',
        'loglevel': 'INFO',
        'traceback': True,
    }

    worker.run(**options)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
