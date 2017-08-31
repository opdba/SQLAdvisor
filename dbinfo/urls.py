# -*- coding: utf-8 -*-
# @Time    : 17-8-27 下午6:23
# @Author  : Wang Chao
from django.conf.urls import url

from . import views

app_name = 'dbsettings'
urlpatterns = [
    url(r'^$', views.dbsettings, name='dbsettings'),
    url(r'^validate/item/name$', views.validate_item_name, name='dbsettings'),

]
