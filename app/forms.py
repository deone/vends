from django import forms
from django.conf import settings
from django.core import serializers
from django.utils.translation import ugettext_lazy as _

from requestor import requestor

class AuthForm(forms.Form):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            data = {
                'username': username,
                'password': password,
            }
            response = requestor(settings.AUTH_URL, data=data)

            for obj in serializers.deserialize('json', response['result']):
                self.user_cache = obj.object

        print self.user_cache
        return self.cleaned_data