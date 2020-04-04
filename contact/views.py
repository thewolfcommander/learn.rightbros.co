from django.shortcuts import render, redirect

from contact.forms import EnrollForDemoForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'contact/home.html', context)


def enroll(request):
    if request.method == 'POST':
        form = EnrollForDemoForm(request.POST or None)
        if form.is_valid():
            enroll = form.save(commit=False)
            enroll.save()
            return redirect('contact:social')
    else:
        form = EnrollForDemoForm()
    context = {
        'form': form
    }
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