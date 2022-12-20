from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class Cliente(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    cpf = models.CharField(max_length=11, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Produto(models.Model):
    nome_produto = models.CharField(max_length=150)
    peso_produto = models.CharField(max_length=100)
    marca_produto = models.CharField(max_length=100)
    descricao_produto = models.TextField()
    imagem_produto = models.ImageField(upload_to='produtos/', blank=False, null=False)

class Plano(models.Model):
    nome_plano = models.CharField(max_length=150)
    descricao_plano = models.TextField()
    valor_plano = models.DecimalField(decimal_places=2,max_digits=5)

class Servico(models.Model):
    nome_servico = models.CharField(max_length=150)
    descricao_sevico = models.TextField()
    imagem_servico = models.ImageField(upload_to='servico/', blank=False, null=False)
    
    class Meta:
        verbose_name_plural = 'Serviços'

class Treinador(models.Model):
    user = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome_treinador = models.CharField(max_length=150)
    email_treinador = models.EmailField()
    telefone_treinador = models.CharField(max_length=100)
    especializacao_treinador = models.CharField(max_length=100)
    imagem_treinador = models.ImageField(upload_to='treinadores/', blank=False, null=False)
    link_twitter = models.CharField(max_length=200, blank=True, null=True)
    link_linkedin = models.CharField(max_length=200, blank=True, null=True)
    link_facebook = models.CharField(max_length=200, blank=True, null=True)
    link_pinterest = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome_treinador + ' (' + self.especializacao_treinador + ')'

    class Meta:
        verbose_name_plural = 'Treinadores'

class Postagem(models.Model):
    titulo_postagem = models.CharField(max_length=150)
    data_postagem = models.DateField(auto_now=True)
    descricao_postagem = models.TextField()
    imagem_postagem = models.ImageField(upload_to='postagens/', blank=False, null=False)
    autor_postagem = models.ForeignKey(Treinador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_postagem + '  por: ' + str(self.autor_postagem)  

    class Meta:
        verbose_name_plural = 'Postagens'
  
class CarrinhoCompras(models.Model):
    produto = models.ForeignKey
    total_pedido = models.DecimalField


