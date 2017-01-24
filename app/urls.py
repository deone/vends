from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, {'template': 'vend_standard.html'}, name='standard'),
    url(r'^accounts/login/$', views.login, name='login'),
]