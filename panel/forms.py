from django import forms


class LoginForm(forms.Form):

    login = forms.CharField(
        max_length=50,
        min_length=2,
        label='Login',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Login",
                "class": "form-control",
                "id": "login",
                "name": "login"
            }
        )
    )
    password = forms.CharField(
        max_length=50,
        min_length=2,
        label='Parol',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Parol",
                "class": "form-control",
                "id": "password",
                "name": "password"
            }
        )
    )
