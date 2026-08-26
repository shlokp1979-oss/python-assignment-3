from django.contrib import admin
from .models import Product, Order, Movie, Review, Playlist


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'seller']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'buyer']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'text']


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']