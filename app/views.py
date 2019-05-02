from django.shortcuts import render,HttpResponse
from app.tasks import send_email
from celery4.celery import app


import time
def email_api(request):

    # send_email()
    result=send_email.delay() # 发送邮件
    # while not result.ready():  # 循环检查任务是否执行完毕
    #     print(time.strftime("%H:%M:%S"))
    #     time.sleep(1)

    # print(result.get())  # 获取任务的返回结果
    # print(result.successful())  # 判断任务是否成功执行

    # send_email()

    return HttpResponse("邮件发送成功 !!! ")


from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
def text(request):

    print("pppppp")
    email = "gmhesat@gmail.com"
    send_mail('subject',  # 邮件标题
              str(datetime.now()),  # 邮件内容
              settings.EMAIL_FROM,  # 源
              [email])  # 目的
    return HttpResponse("xxxxx !!! ")
