from django.shortcuts import render, redirect

from panel.forms import LoginForm
from registration.models import Application


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(
            request=request,
            template_name="panel/login.html",
            context={'form': form}
        )
    elif request.method == "POST":
        data = dict(request.POST)
        login_text = data.get('login')[0]
        password = data.get('password')[0]
        print(login_text, password)
        if login_text != 'leoconsulting' and password != 'leoconsulting777':
            return redirect('/')
        else:
            response = redirect('/panel')
            response.set_cookie(key='verified', value=True, max_age=259200, path='/')
            return response


def panel(request):
    if request.COOKIES.get('verified'):
        apps = Application.objects.filter(status='new').order_by("-created_at")
        return render(
            request=request,
            template_name="panel/admin.html",
            context={
                'apps': apps
            }
        )
    else:
        return redirect('/panel/login')


def pending(request):
    if request.COOKIES.get('verified'):
        apps = Application.objects.filter(status='pending')
        return render(
            request=request,
            template_name="panel/pending.html",
            context={
                'apps': apps
            }
        )
    else:
        return redirect('/panel/login')


def cancelled(request):
    if request.COOKIES.get('verified'):
        apps = Application.objects.filter(status='cancelled')
        return render(
            request=request,
            template_name="panel/cancelled.html",
            context={
                'apps': apps
            }
        )
    else:
        return redirect('/panel/login')


def delete(request, id: int):
    if request.COOKIES.get('verified'):
        Application.objects.filter(pk=id).delete()
        return redirect('/panel')
    else:
        return redirect('/panel/login')


def pend(request, id: int):
    if request.COOKIES.get('verified'):
        Application.objects.filter(id=id).update(status='pending')
        return redirect('/panel/pending')
    else:
        return redirect('/panel/login')


def cancel(request, id: int):
    if request.COOKIES.get('verified'):
        Application.objects.filter(id=id).update(status='cancelled')
        return redirect('/panel/cancelled')
    else:
        return redirect('/panel/login')
