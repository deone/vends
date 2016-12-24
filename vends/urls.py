from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.forms import AuthForm

urlpatterns = [
    url(r'', include('app.urls', namespace='app')),
    url(r'^admin/', admin.site.urls),
]