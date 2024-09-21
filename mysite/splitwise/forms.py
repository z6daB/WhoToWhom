from django import forms
from django.forms import modelformset_factory
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Events, Users, Expenses, User


class CreateEventForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = Events
        fields = ['title']


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username']


UserFormSet = modelformset_factory(Users, form=UserForm, extra=1, can_delete=False)


class ExpenseForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=Users.objects.none(),  # Пустой queryset по умолчанию
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    creator = forms.ModelChoiceField(
        queryset=Users.objects.none(),  # Пустой queryset по умолчанию
        required=True
    )

    class Meta:
        model = Expenses
        fields = ['name', 'creator', 'price', 'members']

    def __init__(self, *args, **kwargs):
        event_id = kwargs.pop('event_id', None)
        super(ExpenseForm, self).__init__(*args, **kwargs)

        if event_id:
            self.fields['members'].queryset = Users.objects.filter(event_id=event_id)
            self.fields['creator'].queryset = Users.objects.filter(event_id=event_id)