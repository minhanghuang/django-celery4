from django.db import models

class xxx(models.Model):

    name = models.CharField(max_length=122,default="")
    tim = models.DateTimeField(auto_now_add=True)