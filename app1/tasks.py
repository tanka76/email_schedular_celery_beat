from celery import shared_task
from time import sleep
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_with_celery():
    subject = 'celery check '
    message = 'Hi this is from celery'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['xyz@gmail.com',]
    send_mail(subject, message , email_from ,recipient_list )

    return None