from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

