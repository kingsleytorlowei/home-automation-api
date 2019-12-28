from celery.schedules import crontab


SCHEDULE = {
    'refresh_all': {
        'task': 'homeautomation.apps.interactions.tasks.refresh_all',
        'schedule': crontab(minute='*/5')
    },

}
