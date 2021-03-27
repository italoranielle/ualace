from django.contrib import admin
from . models import Exercicio, TreinoEx,Treino,ComposicaoCorporal,Medidas,Fotos,Musculos


class ExercicioAdmin(admin.ModelAdmin):
    list_display = ('titulo','tipo')
class MedidasAdmin(admin.ModelAdmin):
    list_display = ('aluno','data')


     
admin.site.register(Exercicio,ExercicioAdmin)
admin.site.register(TreinoEx)
admin.site.register(Treino)
admin.site.register(ComposicaoCorporal)
admin.site.register(Medidas,MedidasAdmin)
admin.site.register(Fotos)
admin.site.register(Musculos)
# Register your models here.
