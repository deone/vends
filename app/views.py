from django.shortcuts import render

from .forms import AuthForm

def login(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthForm()

    context = {'form': form}
    return render(request, 'login.html', context)

def index(request):
    pass