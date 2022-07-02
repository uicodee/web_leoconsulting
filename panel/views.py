from asgiref.sync import async_to_sync
from django.shortcuts import render
from registration.models import Application


def panel(request):
    apps = Application.objects.all()
    return render(
        request=request,
        template_name="panel/admin.html",
        context={
            'apps': apps
        }
    )


async def pending(request):
    # apps = Application.objects.get(status='new')
    # for app in apps:
    #     print(app)
    return render(
        request=request,
        template_name="panel/pending.html"
    )


async def cancelled(request):
    return render(
        request=request,
        template_name="panel/cancelled.html"
    )
