# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Thing(models.Model):
    id = models.IntegerField(primary_key=True)
    task = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
