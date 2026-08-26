from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import OTP
import random


# HOME
def home(request):
    return render(request, 'home.html')


# LOGIN
def login_page(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

        return render(
            request,
            'login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(request, 'login.html')


# WELCOME EMAIL
@login_required
def send_welcome_email(request):

    username = request.user.username
    email = request.user.email

    send_mail(
        subject="Welcome to My Django App",

        message=f"""
Hello {username},

Welcome to our Django application!

We are happy to have you here.

Thank you.
""",

        from_email="noreply@example.com",

        recipient_list=[email],
    )

    return render(
        request,
        'success.html',
        {
            'message': 'Welcome email sent successfully!'
        }
    )


# SEND OTP
@login_required
def send_otp(request):

    if request.method == 'POST':

        phone = request.POST.get('phone')

        otp_code = str(
            random.randint(100000, 999999)
        )

        OTP.objects.create(
            user=request.user,
            phone=phone,
            code=otp_code
        )

        print("OTP:", otp_code)

        return render(
            request,
            'success.html',
            {
                'message': f'OTP sent successfully! Your OTP is {otp_code}'
            }
        )

    return render(
        request,
        'send_otp.html'
    )


# VERIFY OTP
@login_required
def verify_otp(request):

    if request.method == 'POST':

        code = request.POST.get('code')

        otp = OTP.objects.filter(
            user=request.user,
            code=code,
            is_verified=False
        ).first()

        if otp:

            otp.is_verified = True
            otp.save()

            return render(
                request,
                'success.html',
                {
                    'message': 'OTP verified successfully!'
                }
            )

        return render(
            request,
            'verify_otp.html',
            {
                'error': 'Invalid OTP!'
            }
        )

    return render(
        request,
        'verify_otp.html'
    )