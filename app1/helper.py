from django.conf import settings
from django.core.mail import send_mail


def send_mail_without_celery():
    subject = 'celery check '
    message = 'Hi this is without celery'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['xyz@gmail.com',]
    send_mail(subject, message , email_from ,recipient_list )