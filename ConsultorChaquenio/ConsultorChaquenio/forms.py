from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

User = get_user_model()

class RegistroFormulario(UserCreationForm):
    localidad = forms.CharField(required=True)

    class Meta:
        model = User
        fields = [

            'first_name',
            'localidad',
            'username',
            'email',
            'password1',
            'password2',

        ]