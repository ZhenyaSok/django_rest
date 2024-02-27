from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User
from catalog.forms import StyleFormMixin
from django import forms

class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'telegram', 'avatar')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['password'].widget = forms.HiddenInput()