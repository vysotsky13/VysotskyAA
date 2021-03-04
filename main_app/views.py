from django.shortcuts import render, redirect
from .forms import ResponseForm


def index(request):
    return render(request, 'base.html', context={})


def contacts(request):
    form = ResponseForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/contacts/')
    context = {
        'form': form,
    }
    return render(request, "other/contacts.html", context)
