from django.shortcuts import render
from .forms import CadastroClienteForm

# Create your views here.
def index(request):
    return render(request, "index.html");

def cadastro(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST) 
        if form.is_valid():
            form.save()
            form = CadastroClienteForm()
    else:
        form = CadastroClienteForm()

    return render(request,'cadastro.html', { 'form' : form})