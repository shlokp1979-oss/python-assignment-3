from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect

from .models import Product, Order, Review, Playlist


# TASK 1
@login_required
def my_orders(request):

    orders = Order.objects.filter(
        buyer=request.user
    )

    return render(
        request,
        'my_orders.html',
        {
            'orders': orders
        }
    )


# TASK 2
@permission_required(
    'accounts.add_product',
    raise_exception=True
)
def post_product(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        price = request.POST.get('price')

        Product.objects.create(
            name=name,
            price=price,
            seller=request.user
        )

        return redirect('dashboard')

    return render(
        request,
        'post_product.html'
    )


# TASK 3
@permission_required(
    'accounts.add_review',
    raise_exception=True
)
def add_review(request):

    return render(
        request,
        'add_review.html'
    )


# TASK 4
@login_required
def dashboard(request):

    if request.user.groups.filter(
        name='Seller'
    ).exists():

        return render(
            request,
            'seller_dashboard.html'
        )

    elif request.user.groups.filter(
        name='Buyer'
    ).exists():

        return render(
            request,
            'buyer_dashboard.html'
        )

    return render(
        request,
        'normal_dashboard.html'
    )


# TASK 5
@login_required
def playlist_page(request):

    if not request.user.groups.filter(
        name='Admin'
    ).exists():

        return render(
            request,
            'permission_denied.html'
        )

    playlists = Playlist.objects.all()

    return render(
        request,
        'playlist.html',
        {
            'playlists': playlists
        }
    )

    from django.contrib.auth import authenticate


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        return render(
            request,
            'login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(
        request,
        'login.html'
    )