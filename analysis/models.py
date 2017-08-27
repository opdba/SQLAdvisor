# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dbinfo.models import DBinfo
from django.db import models


# Create your models here.


class Analysis(models.Model):
    dbinfo = models.ForeignKey(DBinfo)
    original_sql = models.CharField(max_length=200)  # 原SQL语句
    analysis_result = models.TextField()  # 分析结果
    create_time = models.TimeField(auto_now_add=True)  # 创建时间
