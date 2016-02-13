from django.db import models


class List(models.Model):
    task = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
