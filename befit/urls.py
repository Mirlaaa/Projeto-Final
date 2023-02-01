from django.contrib import admin
from django.urls import path,include, url
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from main.views import * 
from befit import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('main.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)