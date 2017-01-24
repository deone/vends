from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from app.forms import AuthForm

urlpatterns = [
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/login/$', auth_views.login, {
        'template_name': 'login.html',
        'authentication_form': AuthForm
    }, name='login'),
    url(r'', include('app.urls', namespace='app')),
    url(r'^admin/', admin.site.urls),
]