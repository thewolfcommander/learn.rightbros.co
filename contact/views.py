from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'contact/home.html', context)


def enroll(request):
    context = {}
    return render(request, 'contact/enroll.html', context)


def social(request):
    context = {}
    return render(request, 'contact/social.html', context)


def thanks(request):
    context = {}
    return render(request, 'contact/thanks.html', context)


def failed(request):
    context = {}
    return render(request, 'contact/failed.html', context)