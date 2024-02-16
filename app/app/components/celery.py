from django.utils import timezone

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

CELERY_IMPORTS = ('app.tasks',)

CELERY_TASK_TRACK_STARTED = True


CELERY_BEAT_SCHEDULE = {
    'update-reservation-status': {
        'task': 'app.tasks',
        'schedule': timezone.timedelta(seconds=20),
        'options': {
            'scheduler': 'django_celery_beat.schedulers:DatabaseScheduler'
        },
    },
}
