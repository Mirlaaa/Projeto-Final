from django.contrib import admin
from django.urls import path,include
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from main.views import * 
from befit import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_index),
    path('principal/',index, name='index'),
    path('accounts/',conta, name='conta'),
    path('accounts/login/',login, name='login'),
    path('accounts/cadastro',cadastro, name='cadastro'),
    path('logout',logout_app, name='logout'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)