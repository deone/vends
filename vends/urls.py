from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.forms import AuthForm

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, {
        'template_name': 'login.html',
        'authentication_form': AuthForm
    }, name='login'),
    url(r'^admin/', admin.site.urls),
]