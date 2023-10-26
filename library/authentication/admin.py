from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'middle_name', 'last_name', 'email', 'created_at', 'updated_at', 'role', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)