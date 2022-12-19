from django.shortcuts import render, redirect
from .forms import CadastroClienteForm
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.
def redirect_index(request):
    return redirect('index')

def index(request):
    if request.user.is_authenticated:
        print("autenticado")
    return render(request, "index.html")

def conta(request):
    
    return render(request,'cadastro.html')

def login(request):
    print(request.method)

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']        

        if User.objects.filter(email=email).exists():
            nome_usuario = User.objects.filter(email=email).values_list('username', flat=True).get()
        print(nome_usuario)
        user = auth.authenticate(request, username=nome_usuario, password=senha)

        if user is not None:
            auth.login(request, user)
            print('LOGADO!')
            return redirect ('index')
        print(str(request.user))
        print(email, senha)
    return render(request,'cadastro.html',context={'auth': 'sign-in'})
    
def cadastro(request):
    print(request.method)
    if request.method == 'POST':
        nome_completo = request.POST['nome_completo']
        email = request.POST['email']
        cpf = request.POST['cpf']
        senha = request.POST['senha']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Já existe uma conta com esse e-mail, por favor informe outro email!')
            return redirect('cadastro')
            
        user = User.objects.create_user(username=nome_completo,email=email,password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado!')
        print(user)   
        return redirect ('login')
    else:
        return render(request,'cadastro.html',context={'auth': 'sign-up'})
    
def campo_vazio(campo):
  return not campo.strip()
