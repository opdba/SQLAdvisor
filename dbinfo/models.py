# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class DBinfo(models.Model):
    item_name = models.CharField(max_length=100)
    db_host = models.CharField(max_length=100)
    db_port = models.IntegerField()
    db_name = models.CharField(max_length=100)
    db_user = models.CharField(max_length=100)
    db_pwd = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def save(self, **kwargs):
        if kwargs.has_key('request') and self.user is None:
            request = kwargs.pop('request')
            self.user = request.user
        super(DBinfo, self).save(**kwargs)
