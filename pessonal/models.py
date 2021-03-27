from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse 
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Aluno



#----- modelo para treino -------------

class Musculos(models.Model):
    nome = models.CharField(max_length=250)
    valorImagem = models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.nome)

class Exercicio(models.Model):
    titulo = models.CharField(max_length=250)
    musclulo_primario = models.ManyToManyField(Musculos ,related_name='principal')
    musculos_secundarios = models.ManyToManyField(Musculos, related_name='secundario')
    video = models.CharField(max_length=250)
    tipo = models.CharField(max_length=250) #cadio, força...
    equipamento = models.CharField(max_length=250)
    instrucoes = models.TextField()
    
    def __str__(self):
        return str(self.titulo)
    
    def get_absolute_url(self):
        return reverse('exercicodetalhes',args = [self.pk])

class Treino(models.Model):
    aluno = models.ManyToManyField(User)
    titulo = models.CharField(max_length=250)
    validade = models.DateTimeField(default = timezone.now)
    tipo = models.CharField(max_length=50,null=True,blank= True)
    
    def __str__(self):
        return str(self.titulo)


class TreinoEx(models.Model):
    exercicio = models.ForeignKey(Exercicio,on_delete= models.PROTECT)
    treino = models.ForeignKey(Treino,on_delete= models.CASCADE)
    series = models.IntegerField()
    repeticao = models.IntegerField(null = True, blank = True)
    duracao = models.DurationField(null = True, blank= True)
    descanco = models.DurationField()
    
    def get_absolute_url(self):
        return reverse('treinos',args = [self.treino.aluno.pk])
    
    
    
#------------- avaliação ---------------

class ComposicaoCorporal(models.Model):
    aluno = models.ForeignKey(User,on_delete= models.PROTECT)
    peso = models.FloatField()
    musculo_esqueletico = models.FloatField()
    massa_muscular = models.FloatField()
    massa_ossea = models.FloatField()
    idade_corporal = models.IntegerField()
    imc =  models.FloatField()
    gordura_corporal = models.FloatField()
    gordura_visceral = models.IntegerField()
    metabolismo_basal =  models.IntegerField()
    relacao_cintura_quadril = models.FloatField()
    pressao_arterial = models.CharField(max_length=8)
    frequencia_cardiaca = models.IntegerField()
    data = models.DateTimeField(default = timezone.now)
    observacao = models.TextField()
    
    def get_absolute_url(self):
        return reverse('Composidelahes',args = [self.pk])
        #return f"composicaoCorporaldetalhe/{self.pk}/"
    
class Medidas(models.Model):
    aluno = models.ForeignKey(User, on_delete = models.PROTECT)
    pescoco = models.FloatField()
    ombros = models.FloatField()    
    torax = models.FloatField()
    abdmen = models.FloatField()
    quadril = models.FloatField()
    cintura = models.FloatField()
    braco_esquerdo = models.FloatField()    
    braco_esquerdo_c = models.FloatField()
    braco_direito = models.FloatField()
    braco_direito_c = models.FloatField()
    perna_esquerda_m =  models.FloatField()
    perna_esquerda_d = models.FloatField()
    perna_esquerda_p = models.FloatField()
    perna_direita_m =  models.FloatField()
    perna_direita_d = models.FloatField()
    perna_direita_p = models.FloatField()
    panturrilha_esquerda = models.FloatField()
    panturrilha_direita = models.FloatField()
    data = models.DateTimeField(default = timezone.now)
    
    def get_absolute_url(self):
        return reverse('medidasdelahes',args = [self.pk])
    
    def __str__(self):
        return str(self.aluno)
    
class Fotos(models.Model):
    aluno = models.ForeignKey(User, on_delete = models.PROTECT)
    foto = models.ImageField(upload_to="corpo/")
    data = models.DateTimeField(default = timezone.now)