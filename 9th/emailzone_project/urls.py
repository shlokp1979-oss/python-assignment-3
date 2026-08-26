"""
URL configuration for emailzone_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from emailzone.views import (
    test_email,
    send_password_reset_email,
    send_order_confirmation,
    send_ipl_email,
)


urlpatterns = [

    path('admin/', admin.site.urls),

    path(
        'test-email/',
        test_email,
        name='test_email'
    ),

    path(
        'order-email/',
        send_order_confirmation,
        name='order_email'
    ),

    path(
        'ipl-email/',
        send_ipl_email,
        name='ipl_email'
    ),
]