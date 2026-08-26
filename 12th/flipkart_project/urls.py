"""
URL configuration for flipkart_project project.

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

from products.views import (
    product_list,
    add_product,
    edit_product,
    delete_product
)


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        product_list,
        name='product_list'
    ),

    path(
        'add/',
        add_product,
        name='add_product'
    ),

    path(
        'edit/<int:id>/',
        edit_product,
        name='edit_product'
    ),

    path(
        'delete/<int:id>/',
        delete_product,
        name='delete_product'
    ),
]
