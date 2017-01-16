from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from .forms import AuthForm

urlpatterns = [
    url(r'^$', views.index, {'template': 'vend_standard.html'}, name='standard'),
    url(r'^accounts/login/$', auth_views.login, {
        'template_name': 'login.html',
        'authentication_form': AuthForm
    }, name='login'),
]