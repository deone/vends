from django.conf.urls import url

from . import views
from .forms import AuthForm

urlpatterns = [
        url(r'^login$', views.login, name='login'),
        url(r'^$', views.index, name='index'),
    ]