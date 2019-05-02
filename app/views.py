from django.shortcuts import HttpResponse
from app.tasks import send_email



def email_api(request):

    result = send_email.delay() # 发送邮件
    result.get()

    return HttpResponse("邮件发送成功 !!! ")
