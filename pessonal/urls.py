# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:25:08 2020

@author: pc_lab
"""

from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name = 'home'),
    path('dash/', views.dash, name = 'dash'),
    path('composicaoCorporal/<int:aluno>', views.composiList, name = 'ComposiList'),
    path('composicaoCorporaldetalhe/<int:pk>', views.ComposiDetail.as_view(), name = 'Composidelahes'),
    path('composicaoCorporalnovo/', views.ComposiCreate.as_view(), name = 'Composinovo'),
    path('composicaoCorporaleditar/<int:pk>', views.ComposiEdit.as_view(), name = 'Composiedit'),
    path('medidas/<int:aluno>', views.medidasList, name = 'medidasList'),
    path('medidasnovo/', views.MedidasCreate.as_view(), name = 'medidasnovo'),
    path('medidasdetalhe/<int:pk>', views.MedidasDetail.as_view(), name = 'medidasdelahes'),
    path('medidaseditar/<int:pk>', views.MedidasEdit.as_view(), name = 'medidasedit'),
    
    path('exercicodetalhe/<int:pk>', views.exercicioDetail.as_view(), name = 'exercicodetalhes'),
    path('exercicionovo/', views.exercicioCreate.as_view(), name = 'exercicionovo'),
    path('exercicioeditar/<int:pk>', views.exercicioEdit.as_view(), name = 'exercicioedit'),
    path('exerciciolist/', views.exercicioList.as_view(), name = 'exerciciolist'),
    
    path('treinosP/', views.listTreinoPadrao, name = 'treinosP'),
    path('treinoPedit/<int:pk>', views.TreinoPadraoEdit.as_view(), name = 'treinoPedit'),
    path('treinos/<int:aluno>', views.listTreino, name = 'treinos'),
    path('novotreino/<int:aluno>', views.treinoNew, name = 'novotreino'),
    path('novotreinoP/', views.treinoNewPadrao, name = 'novotreinoP'),
    path('deletartreino/<int:pk>', views.TreinoDelete.as_view(), name = 'deltreino'),
    path('novotreinoexercicio/<int:treino>', views.treinoexNew, name = 'novotreinoex'),
    path('Editarteinoexercicio/<int:pk>', views.TreinoexEdit.as_view(), name = 'edittreinoex'),
    path('deletartreinoexercicio/<int:pk>', views.TreinoexDelete.as_view(), name = 'deltreinoex'),
    
    
]


