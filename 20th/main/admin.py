from django.contrib import admin
from .models import Restaurant
from .models import UserProfile

admin.site.register(Restaurant)
admin.site.register(UserProfile)