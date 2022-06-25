from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Application


def index(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            Application.objects.create(**form.cleaned_data)
            request.session['from_reg'] = True
            return redirect('/thanks')

    else:
        form = RegisterForm()

    return render(
        request=request,
        template_name='registration/register.html',
        context={'form': form}
    )
