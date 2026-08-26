from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import random

from .models import Restaurant, UserProfile


# TASK 1
def restaurant_search(request):

    cuisine = request.GET.get('cuisine', '')
    location = request.GET.get('location', '')

    restaurants = Restaurant.objects.all()

    if cuisine:
        restaurants = restaurants.filter(
            cuisine__icontains=cuisine
        )

    if location:
        restaurants = restaurants.filter(
            location__icontains=location
        )

    return render(
        request,
        'search.html',
        {'restaurants': restaurants}
    )


# TASK 2 - Login
def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            otp = str(random.randint(100000, 999999))

            request.session['otp'] = otp
            request.session['username'] = username
            request.session.set_expiry(180)

            print("OTP:", otp)

            return render(
                request,
                'verify_otp.html',
                {'otp': otp}
            )

        return render(
            request,
            'login.html',
            {'error': 'Invalid username or password'}
        )

    return render(request, 'login.html')


# TASK 2 - OTP
def verify_otp(request):

    if request.method == 'POST':

        entered_otp = request.POST.get('otp')
        saved_otp = request.session.get('otp')

        if entered_otp == saved_otp:

            username = request.session.get('username')

            user = User.objects.get(
                username=username
            )

            login(request, user)

            request.session.pop('otp', None)

            return render(
                request,
                'dashboard.html',
                {'username': username}
            )

        return render(
            request,
            'verify_otp.html',
            {'error': 'Invalid OTP'}
        )

    return render(request, 'verify_otp.html')


# TASK 3 - Profile
def profile(request):

    if not request.user.is_authenticated:

        return render(
            request,
            'login.html',
            {'error': 'Please login first'}
        )

    profile_data, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        request.user.first_name = request.POST.get('name')
        request.user.email = request.POST.get('email')
        request.user.save()

        profile_data.address = request.POST.get('address')

        if request.FILES.get('profile_picture'):
            profile_data.profile_picture = request.FILES.get(
                'profile_picture'
            )

        profile_data.save()

    return render(
        request,
        'profile.html',
        {'profile': profile_data}
    )


# TASK 4 - Google Map
def map_page(request):

    return render(
        request,
        'map.html'
    )

def home(request):
    return render(request, 'home.html')