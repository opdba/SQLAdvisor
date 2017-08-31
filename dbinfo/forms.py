# -*- coding: utf-8 -*-
# @Time    : 17-8-31 下午1:41
# @Author  : Wang Chao
from django import forms
from .models import DBinfo


class DBCreate(forms.ModelForm):

    class Meta:
        model = DBinfo
        exclude = ["user"]
