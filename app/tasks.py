from celery import shared_task
from celery import task
from app.models import xxx
from datetime import datetime
from time import sleep
now = datetime.now()


@shared_task
def text(a,b):

    c = a+b
    xxx.objects.create(
        name = c,
    )


    return "celery4.3"


from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime





from celery4.celery import app

@shared_task
def send_email():

    print("邮件发送中...")
    sleep(5)
    xxx.objects.create(
        name="发送邮件",
    )
    email = "1097329291@qq.com"
    send_mail('subject',  # 邮件标题
              "oooo",  # 邮件内容
              settings.EMAIL_FROM,  # 源
              [email])  # 目的

    return "jjjjj"






