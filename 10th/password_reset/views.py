import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import ForgotPasswordForm, OTPForm


def forgot_password_view(request):

    if request.method == 'POST':

        form = ForgotPasswordForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            # Generate 6-digit OTP
            otp = str(random.randint(100000, 999999))

            # Store OTP in session
            request.session['otp'] = otp
            request.session['otp_email'] = email

            # OTP expires after 5 minutes
            request.session.set_expiry(300)

            # Send OTP
            send_mail(
                'Password Reset OTP',
                f'Your password reset OTP is: {otp}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            return redirect('verify_otp')

    else:
        form = ForgotPasswordForm()

    return render(
        request,
        'forgot_password.html',
        {'form': form}
    )


def verify_otp_view(request):

    if request.method == 'POST':

        form = OTPForm(request.POST)

        if form.is_valid():

            entered_otp = form.cleaned_data['otp']
            stored_otp = request.session.get('otp')

            if entered_otp == stored_otp:

                # OTP used successfully
                request.session.pop('otp', None)

                return render(
                    request,
                    'success.html'
                )

            else:

                return render(
                    request,
                    'verify_otp.html',
                    {
                        'form': form,
                        'error': 'Invalid OTP. Please try again.'
                    }
                )

    else:
        form = OTPForm()

    return render(
        request,
        'verify_otp.html',
        {'form': form}
    )