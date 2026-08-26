from django.shortcuts import render
from .forms import SignupForm


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'signup_success.html')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })


def welcome(request):
    return render(request, 'welcome.html')