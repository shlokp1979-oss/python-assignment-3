from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    login_view,
    dashboard,
    my_orders,
    post_product,
    add_review,
    playlist_page
)


urlpatterns = [

    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        'my-orders/',
        my_orders,
        name='my_orders'
    ),

    path(
        'post-product/',
        post_product,
        name='post_product'
    ),

    path(
        'add-review/',
        add_review,
        name='add_review'
    ),

    path(
        'playlist/',
        playlist_page,
        name='playlist'
    ),
]