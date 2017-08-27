# -*- coding: utf-8 -*-
# @Time    : 17-8-27 下午4:39
# @Author  : Wang Chao

from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.analysis, name='analysis'),
]
