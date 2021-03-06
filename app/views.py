from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request, template='vend_standard.html'):
    return render(request, template)