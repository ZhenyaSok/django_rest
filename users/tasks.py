from datetime import datetime, timedelta
import logging
from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def deactivate_user():
    users = User.objects.filter(
        last_login__lt=datetime.now() - timedelta(days=30),
        is_staff=False,
        is_superuser=False
    )
    for user in users:
        logging.info(f'Пользователь {user} заблокирован')
    users.update(is_active=False)