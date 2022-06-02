# from django.contrib.auth import get_user_model
#
# from config import celery_app
#
# User = get_user_model()
#
#
# @celery_app.task()
# def get_users_count():
#     """A pointless Celery task to demonstrate usage."""
#     return User.objects.count()



from __future__ import absolute_import, unicode_literals

from celery import shared_task

@shared_task
def add(x, y):
    print(x+y)
    return x + y