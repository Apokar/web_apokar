#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 14:55
# @Author  : Apokar
# @Email   : Apokar@163.com
# @File    : urls.py

from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
