from django.shortcuts import render, redirect
from .forms import RestaurantForm


def add_restaurant(request):

    if request.method == 'POST':

        form = RestaurantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = RestaurantForm()

    return render(request, 'restaurant_form.html', {
        'form': form
    })


def success(request):
    return render(request, 'success.html')