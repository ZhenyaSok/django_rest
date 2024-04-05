from celery import shared_task
from django.core.mail import send_mail

from config import settings
from lms.models import Subscribe, Course


@shared_task
def send_mail_sub(course_id, *args, **kwargs):
    course = Course.objects.get(pk=course_id)
    subscriptions = Subscribe.objects.filter(course_id=course_id)
    for subscription in subscriptions:
        print(f'3!!!!!!!!{subscription.user.email}')
        send_mail(subject=f"Новости",
                  message=f"Хорошие новости о курсе - , который вас интересует!",
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[subscription.user.email],
                  # fail_silently=False
                  )



