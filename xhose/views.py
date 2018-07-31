from django.shortcuts import render
from .forms import *


def xhose(request):
    if request.method != 'POST':
        form = BuyForm()
    else:
        form = BuyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'xhose/success.html', locals())
    return render(request, 'xhose/xhose.html', locals())
