from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["last_name", "first_name", "username", "email", "role", "is_staff"]

    fieldsets = UserAdmin.fieldsets + (
        ("School Profile", {"fields": ("role", "course")}),
    )
