from django.shortcuts import HttpResponse
from app.tasks import send_email



def email_api(request):

    send_email.delay() # 发送邮件

    return HttpResponse("邮件发送成功 !!! ")
