"""Trying dropzone.js lib http://www.dropzonejs.com/"""

from django.db import models


class UploadFile(models.Model):
    file = models.FileField(upload_to='media/')
