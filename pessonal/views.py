from django.contrib.auth.models import User
from django.shortcuts import render, redirect , get_object_or_404
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from . models import ComposicaoCorporal , Treino, TreinoEx ,Medidas ,Exercicio, Fotos
from .forms import TreinoForm , TreinoExForm, CompForm,  ImageUploadForm
from django.urls import reverse_lazy
from django.core import serializers
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def home(request):
    return render(request,'perssonal/home.html')

@login_required
def dash(request):
    composi = ComposicaoCorporal.objects.filter(aluno_id = request.user).values()             # 
    peso = [entry['peso'] for entry in composi]  
    ossea = [entry['massa_ossea'] for entry in composi]  
    musculo = [entry['massa_muscular'] for entry in composi]
    gordura = [entry['gordura_corporal'] for entry in composi]
    data = [entry['data'].strftime("%d-%m-%Y") for entry in composi]  
    teste = {'peso':peso,'data':data,'musculo':musculo, 'gordura':gordura ,'ossea':ossea }
    data = {'teste':teste,'peso':peso} 
    return render(request,'perssonal/dash.html',data)


#---------------- Exercicios

class exercicioList(LoginRequiredMixin,ListView):
    model = Exercicio
    template_name = 'perssonal/exercicio_list.html' 


class exercicioDetail(LoginRequiredMixin,DetailView):
    model = Exercicio
    template_name = 'perssonal/exercicio_detail.html' 


    
    
    
class exercicioCreate(PermissionRequiredMixin,CreateView):
    permission_required = 'pessonal.add_exercicio'
    model = Exercicio
    template_name = 'perssonal/exercicio_create.html'  
    fields = '__all__'
    
    
class exercicioEdit(PermissionRequiredMixin,UpdateView):
    permission_required = 'pessonal.change_exercicio'
    model = Exercicio
    template_name = 'perssonal/exercicio_edit.html'  
    fields = '__all__'
    




#----------------Composição corporal

@login_required
def composiList(request,aluno):
        usuario = request.user
        if usuario.is_superuser:
            usuario = User.objects.filter(pk = aluno).first()
        composi = ComposicaoCorporal.objects.filter(aluno_id = usuario)
        data = {'object_list':composi} 
        return render(request, 'perssonal/composicao_list.html',data)


class ComposiDetail(LoginRequiredMixin,DetailView):
    model = ComposicaoCorporal
    template_name = 'perssonal/composicao_detail.html'     
    
    
class ComposiCreate(PermissionRequiredMixin,CreateView):
    permission_required = 'pessonal.add_ComposicaoCorporal'
    model = ComposicaoCorporal
    template_name = 'perssonal/composicao_create.html'  
    fields = '__all__'
    
    
class ComposiEdit(PermissionRequiredMixin,UpdateView):
    permission_required = 'pessonal.change_ComposicaoCorporal'
    model = ComposicaoCorporal
    form_class = CompForm
    template_name = 'perssonal/composicao_edit.html'  
    
    
#------------------medidas ------------
@login_required
def medidasList(request,aluno):
        usuario = request.user
        if usuario.is_superuser:
            usuario = User.objects.filter(pk = aluno).first()
        medidas = Medidas.objects.filter(aluno_id = usuario)
        data = {'object_list':medidas} 
        return render(request, 'perssonal/medidas_list.html',data)


class MedidasDetail(LoginRequiredMixin,DetailView):
    model = Medidas
    template_name = 'perssonal/medidas_detail.html'  
    
    
class MedidasCreate(PermissionRequiredMixin,CreateView):
    permission_required = 'pessonal.add_medidas'
    model = Medidas
    template_name = 'perssonal/medidas_create.html'  
    fields = '__all__'
    
class MedidasEdit(PermissionRequiredMixin,UpdateView):
    permission_required = 'pessonal.change_medidas'
    model = Medidas
    template_name = 'perssonal/medidas_edit.html'  
    fields = '__all__'

#------------------treino ------------
@login_required
def listTreino(request,aluno):
    #fazer condição de usuario ou de admin
    #the_aluno = User.objects.get(username='italo')
    treino = Treino.objects.filter(aluno = aluno)
    ex = TreinoEx.objects.filter(treino__in = treino)
    treform = TreinoForm()
    exform = TreinoExForm()
    data = {'treinos':treino,'exs':ex,'treform':treform,'aluno':aluno ,'exform':exform} 
    return render(request, 'perssonal/treino_list.html',data)


@permission_required('pessonal.view_treino')
def listTreinoPadrao(request):
    treino = Treino.objects.filter(tipo = "padrao")
    ex = TreinoEx.objects.filter(treino__in = treino)
    treform = TreinoForm()
    exform = TreinoExForm()
    data = {'treinos':treino,'exs':ex,'treform':treform,'exform':exform} 
    return render(request, 'perssonal/treino_list _padrao.html',data)

class TreinoPadraoEdit(PermissionRequiredMixin,UpdateView):
    permission_required = 'pessonal.change_treino'
    model = Treino
    template_name = 'perssonal/treino_edit.html'  
    fields = '__all__'
    success_url = '/treinosP'





#---------Montar Treino-----------
#-somente admin -

@permission_required('pessonal.add_treino')
def treinoNew(request,aluno):
    form = TreinoForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.tipo = "exclusivo"
        post.save()
        post.aluno.add(aluno)
    return redirect('/treinos/'+str(aluno))


@permission_required('pessonal.add_treino')
def treinoNewPadrao(request):
    form = TreinoForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.tipo = "padrao"
        post.save()
    return redirect('/treinosP/')


class TreinoDelete(PermissionRequiredMixin,DeleteView): 
    permission_required = 'pessonal.delete_treino'
    model = Treino 
    template_name = 'perssonal/Treino_delete.html' 
    def get_success_url(self):
    # Assuming there is a ForeignKey from Comment to Post in your model
        post = self.object.aluno.pk
        return reverse_lazy( 'treinos', kwargs={'aluno': post})


@permission_required('pessonal.add_treino')
def treinoexNew(request,treino):
    form = TreinoExForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        treinoOBJ = Treino.objects.filter(id = treino)[0]
        post.treino = treinoOBJ
        post.save()
    return redirect('/treinos/'+str(treinoOBJ.aluno.pk))


class TreinoexEdit(PermissionRequiredMixin,UpdateView):
    permission_required = 'pessonal.change_treinoEx'
    model = TreinoEx
    form_class = TreinoExForm
    template_name = 'perssonal/TreinoEx_edit.html'  
    
    
    

class TreinoexDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'pessonal.delete_treinoEx'
    model = TreinoEx 
    template_name = 'perssonal/TreinoEx_delete.html' 
    def get_success_url(self):
    # Assuming there is a ForeignKey from Comment to Post in your model
        post = self.object.treino.aluno.pk

        return reverse_lazy( 'treinos', kwargs={'aluno': post})
    
    


# =============================================================================
# 
# class CreatePostView(CreateView): # new
#     model = Fotos
#     form_class = ImageUploadForm
#     template_name = 'perssonal/images.html'
#     success_url = reverse_lazy('home')
# =============================================================================
