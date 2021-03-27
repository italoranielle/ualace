from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .models import Aluno
from .forms import UserForm, UserAdminForm, AlunoForm




class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
class CreateAluno(generic.CreateView):
    model = Aluno
    template_name = 'accounts/criarAluno.html'  
    fields = '__all__'

    
@login_required    
def UserView(request):
    user = User.objects.filter(pk = request.user.pk)
    data = {'usuario':user } 
    return render(request, 'accounts/profile.html',data) 
    

def alunoView(request,aluno):
    user = User.objects.filter(pk = aluno)
    data = {'usuario':user } 
    
   
    return render(request, 'accounts/profile.html',data) 

@login_required 
def PasswordReset(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('change_password')
        else:
            messages.error(request, 'Erro! Tente novamente.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/resetUser.html', {
        'form': form
    })


def update_aluno(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = AlunoForm(request.POST,request.FILES, instance=request.user.aluno)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('/accounts/profile/')
        else:
            pass
            #messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = AlunoForm(instance=request.user.aluno)
    return render(request, 'accounts/upAluno.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    

def adm_update_aluno(request,aluno):
    user = User.objects.filter(pk = aluno).first()
    if request.method == 'POST':
        user_form = UserAdminForm(request.POST, instance=user)
        profile_form = AlunoForm(request.POST,request.FILES, instance=user.aluno)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('/accounts/alunos/')
        else:
            pass
            #messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserAdminForm(instance=user)
        profile_form = AlunoForm(instance=user.aluno)
    return render(request, 'accounts/upAluno.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def alunos(request):
    user = User.objects.all()
    data = {'alunos':user } 
    return render(request, 'accounts/alunos.html',data) 