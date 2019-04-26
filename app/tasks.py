from celery import shared_task
from app.models import xxx
from datetime import datetime

now = datetime.now()


@shared_task
def text(a,b):

    c = a+b
    xxx.objects.create(
        name = c,
    )


    return "celery4.3"


