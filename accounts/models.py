from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse 



class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True)
    altura = models.FloatField(null=True)
    foto = models.ImageField(upload_to="perfil/", null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('aluno_profile',args = [self.user.pk])
    
    def idade(self):
        hoje = timezone.now()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))


@receiver(post_save, sender = User)
def create_user_colaborador(sender, instance, created,**kwargs):
    if created:
        Aluno.objects.create(user=instance)
        
@receiver(post_save, sender = User)
def save_user_colaborador(sender, instance,**kwargs):
        instance.aluno.save()
        
        