from django.contrib import admin
from django.urls import path
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
     path('cadastro/', cadastro, name='cadastro')
]
