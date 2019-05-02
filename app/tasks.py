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


@shared_task
def send_email():

    print("邮件发送中...")
    sleep(10)
    xxx.objects.create(
        name="发送邮件",
    )

    return "邮箱发送成功!!!"






