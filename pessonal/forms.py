# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:41:20 2020

@author: pc_lab
"""


from django.forms import ModelForm
from .models import Treino , TreinoEx, ComposicaoCorporal, Fotos,Exercicio


 
class TreinoForm(ModelForm):
    class Meta:           
        model = Treino
        #fields = '__all__'
        exclude = ['aluno','tipo']
# =============================================================================
#         labels = {
#             'componente':('Equipamento/ Sub Equipamento '),
#         }
# =============================================================================
class TreinoExForm(ModelForm):
    class Meta:           
        model = TreinoEx
        #fields = '__all__'
        exclude = [ 'treino']
  
 
class CompForm(ModelForm):
    class Meta:
        model = ComposicaoCorporal
        exclude = ('aluno',)



class ImageUploadForm(ModelForm):
    class Meta:
        model = Fotos
        fields = '__all__'


