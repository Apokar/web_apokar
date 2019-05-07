#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-02 15:47
# @Author  : Apokar
# @Email   : Apokar@163.com
# @File    : blog_tags.py

from django import template
from ..models import Post, Category

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()
