from travels import urls
import travels
from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('', include(travels.urls)),
    path('admin/', admin.site.urls),
   
]
