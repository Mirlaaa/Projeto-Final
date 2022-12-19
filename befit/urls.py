from django.contrib import admin
from django.urls import path,include
from main.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_index),
    path('principal/', include('main.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
