from django.db import models

class Cadastro_Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    cpf = models.CharField(max_length=100)
    senha = models.IntegerField()

# class Produto(models.Model):
#     nome = models.CharField(max_length=150)
#     peso = models.CharField(max_length=100)
#     marca = models.CharField(max_length=100)
#     descricao = models.TextField()
#     # imagem

# class Plano(models.Model):
#     nome = models.CharField(max_length=150)
#     descricao = models.TextField()
#     valor = models.IntegerField()

# class Servico(models.Model):
#     nome = models.CharField(max_length=150)
#     descricao = models.TextField()
#     # imagem
    
# class Treinador(models.Model):
#     nome = models.CharField(max_length=150)
#     email = models.EmailField()
#     telefone = models.IntegerField()
#     especializacao = models.CharField(max_length=100)
#     # imagem
#     # link

# class Postagem(models.Model):
#     titulo = models.CharField(max_length=150)
#     autor = models.CharField(max_length=100)
#     data_postagem = models.DateField()
#     descricao = models.TextField()
#     # imagem  
  