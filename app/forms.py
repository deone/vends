from django import forms
from django.conf import settings
from django.core import serializers
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from requestor import requestor

class AuthForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            data = {
                'username': username,
                'password': password,
            }
            response = requestor(settings.AUTH_URL, data=data)

            for obj in serializers.deserialize('json', response.json()['result']):
                # save object locally
                obj.save()
                self.user_cache = obj.object

            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data