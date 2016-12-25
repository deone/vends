from django.conf import settings
from django.shortcuts import render

from .forms import AuthForm

from requestor import requestor

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        data = {
            'username': username,
            'password': password,
        }

        response = requestor(settings.AUTH_URL, data=data)
    else:
        pass

    form = AuthForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def index(request):
    pass