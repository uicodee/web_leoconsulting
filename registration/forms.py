from django import forms

from .models import Region


class RegisterForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        min_length=2,
        label='Имя',
        widget=forms.TextInput(attrs={"placeholder": "Ism"})
    )
    surname = forms.CharField(
        max_length=100,
        min_length=2,
        label='Фамилия',
        widget=forms.TextInput(attrs={"placeholder": "Familiya"})
    )
    age = forms.IntegerField(
        max_value=60,
        min_value=16,
        label='Возраст',
        widget=forms.NumberInput(attrs={"placeholder": "Yosh"})
    )
    region = forms.ModelChoiceField(empty_label=None, label='Регион', queryset=Region.objects.all())
    phone_number = forms.CharField(
        max_length=13,
        min_length=13,
        label='Номер телефона',
        widget=forms.TextInput(attrs={"placeholder": "Telefon raqamingiz"})
    )

