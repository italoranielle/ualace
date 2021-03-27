# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 09:22:21 2020

@author: uia89236
"""


from django.urls import path
from . import views



urlpatterns = [
    
     
     path('signup/', views.SignUpView.as_view(), name = 'signup'),
     path('profile/', views.UserView, name = 'user_profile'),
     path('alunoprofile/<int:aluno>', views.alunoView, name = 'aluno_profile'),
     path('reset/', views.PasswordReset, name = 'reset_pw'),
     path('alunos/', views.alunos, name = 'alunos'),
     path('novoAluno/', views.CreateAluno.as_view(), name = 'novo_aluno'),
     path('updateAluno/', views.update_aluno, name = 'update_aluno'),
     path('admupdateAluno/<int:aluno>', views.adm_update_aluno, name = 'adm_update_aluno'),
]
