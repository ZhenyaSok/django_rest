from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User

from django import forms

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'city', 'avatar')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['password'].widget = forms.HiddenInput()