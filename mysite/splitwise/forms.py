from django import forms
from django.forms import modelformset_factory
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Events, Users


class CreateEventForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = Events
        fields = ['title']


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username']  # Только поле username


UserFormSet = modelformset_factory(Users, form=UserForm, extra=1, can_delete=True)
