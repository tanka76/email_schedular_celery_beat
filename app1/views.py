from app1.tasks import sleepy
from django.shortcuts import render
from django.http import HttpResponse
from app1.tasks import sleepy
from django.conf import settings
from django.core.mail import send_mail
from app1.helper import send_mail_without_celery
from app1.tasks import send_mail_with_celery
# Create your views here.

def index(request):

    send_mail_with_celery.delay()
    return HttpResponse("<h1>hello from  celery</h1>")



