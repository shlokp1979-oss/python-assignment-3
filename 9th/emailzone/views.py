from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string


def test_email(request):
    send_mail(
        'Test Email from Django',
        'Hello! This is a test email sent using Django.',
        'yourgmail@gmail.com',
        ['yourgmail@gmail.com'],
        fail_silently=False,
    )

    return render(request, 'success.html')


def send_password_reset_email(request, user_email):

    subject = 'Password Reset Request'

    message = """
Hello,

We received a request to reset your password.

Click the password reset link below to create a new password:

https://example.com/reset-password/

If you did not request this, please ignore this email.

Thank you.
"""

    send_mail(
        subject,
        message,
        'yourgmail@gmail.com',
        [user_email],
        fail_silently=False,
    )

    return render(request, 'success.html')


def send_order_confirmation(request):

    context = {
        'user_name': 'Shlok',
        'restaurant': 'Pizza Palace',
        'item': 'Margherita Pizza',
        'quantity': 2,
        'amount': 599,
    }

    html_content = render_to_string(
        'order_confirmation.html',
        context
    )

    subject = 'Your Food Order is Confirmed! 🍕'

    text_content = (
        'Hello Shlok, your order from Pizza Palace '
        'has been confirmed.'
    )

    email = EmailMultiAlternatives(
        subject,
        text_content,
        'yourgmail@gmail.com',
        ['yourgmail@gmail.com'],
    )

    email.attach_alternative(
        html_content,
        'text/html'
    )

    email.send()

    return render(request, 'success.html')


def send_ipl_email(request):

    subject = '🏏 Welcome to IPL Fantasy League! Build Your Dream Team!'

    text_content = """
Welcome to IPL Fantasy League!

Create your dream team, choose your favorite players,
earn points and compete with your friends.

Let the fantasy cricket begin!
"""

    html_content = """
    <html>
    <body style="font-family: Arial;">

        <h1>🏏 Welcome to IPL Fantasy League!</h1>

        <h2>Build Your Dream Team!</h2>

        <p>
            Pick your favorite cricket stars and create
            your ultimate fantasy team.
        </p>

        <p>
            Earn points, compete with your friends,
            and climb the leaderboard!
        </p>

        <h3>Let the Fantasy Cricket Begin! 🔥</h3>

    </body>
    </html>
    """

    email = EmailMultiAlternatives(
        subject,
        text_content,
        'yourgmail@gmail.com',
        ['yourgmail@gmail.com'],
    )

    email.attach_alternative(
        html_content,
        'text/html'
    )

    email.send()

    return render(request, 'success.html')