from django.shortcuts import render
from .forms import AddRestaurantForm


def add_restaurant(request):

    if request.method == "POST":
        form = AddRestaurantForm(request.POST)

        if form.is_valid():
            return render(
                request,
                'success.html',
                {
                    'data': form.cleaned_data
                }
            )

    else:
        form = AddRestaurantForm()

    return render(request, 'add_restaurant.html', {
        'form': form
    })