from django.shortcuts import render, redirect


def thanks(request):
    r = request.session.get('from_reg', False)
    if r:
        request.session['from_reg'] = False
        return render(
            request=request,
            template_name="thanks/thanks.html"
        )
    else:
        return redirect('/')
