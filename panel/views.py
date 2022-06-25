from django.shortcuts import render


def panel(request):
    return render(
        request=request,
        template_name="panel/admin.html"
    )


async def pending(request):
    return render(
        request=request,
        template_name="panel/pending.html"
    )


async def cancelled(request):
    return render(
        request=request,
        template_name="panel/cancelled.html"
    )
