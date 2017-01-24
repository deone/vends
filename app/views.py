from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import AuthForm

def login(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
    else:
        form = AuthForm()

    context = {'form': form}
    return render(request, 'login.html', context)

@login_required
def index(request):
    pass