from django.contrib import admin
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    list_display = ['name', 'cuisine', 'rating']

    search_fields = ['name', 'cuisine']

    list_filter = ['cuisine']