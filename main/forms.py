from django import forms
from main.models import Cadastro_Cliente

class CadastroClienteForm(forms.ModelForm):
    class Meta:
        model=Cadastro_Cliente
        fields = '__all__'
        
        # widgets = {
        #     'minicursos': forms.CheckboxSelectMultiple(),
        #     'sexo': forms.RadioSelect(),
        #     'data_nascimento': forms.TimeInput(attrs={'type':'date'}),
        # }