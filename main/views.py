from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import Cliente
from befit import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def redirect_index(request):
    return redirect('index')

@login_required
def index(request):
    return render(request, "index.html")

def conta(request):
    return render(request,'cadastro.html')

def cadastro(request):
    print(request.method)
    if request.method == 'POST':
        nome_completo = request.POST['nome_completo']
        email = request.POST['email']
        cpf = request.POST['cpf']
        senha = request.POST['senha']

        if Cliente.objects.filter(email=email).exists():
            messages.error(request, 'Já existe uma conta com esse e-mail, por favor informe outro email!')
            return redirect('cadastro')
        else:    
            user = Cliente.objects.create_user(username=nome_completo,email=email,cpf=cpf,password=senha)
            user.save()
            messages.success(request, 'Usuário cadastrado!')
            return redirect ('login')
    else:
        return render(request,'cadastro.html',context={'auth': 'sign-up'})
    
def login(request):
    print(request.method)

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']        

        if Cliente.objects.filter(email=email).exists():
            user = auth.authenticate(request, email=email, password=senha)

            if user is not None:
                auth.login(request, user)
                return redirect (settings.LOGIN_REDIRECT_URL)
            else:
                messages.error(request,'E-mail e/ou senha incorretos!')
    return render(request,'cadastro.html',context={'auth': 'sign-in'})
    
def logout_app(request):
    logout(request)
    return redirect('login')

def campo_vazio(campo):
  return not campo.strip()

