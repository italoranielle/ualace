# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:36:25 2020

@author: pc_lab
"""
from django.forms import ModelForm
from .models import Aluno
from django.contrib.auth.models import User



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserAdminForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','is_active')

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        exclude = ['user']