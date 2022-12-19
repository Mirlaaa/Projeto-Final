from django.urls import path
from .views import *

urlpatterns = [
  path('',index, name='index'),
  path('account/',conta, name='conta'),
  path('account/login',login, name='login'),
  path('account/cadastro',cadastro, name='cadastro'),
  
]