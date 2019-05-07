#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 14:45
# @Author  : Apokar
# @Email   : Apokar@163.com
# @File    : forms.py


from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']

