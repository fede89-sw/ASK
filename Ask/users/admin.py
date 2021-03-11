from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# creo CustomUserAdmin dato che ho creato CustomUser
class CustomUserAdmin(UserAdmin):
    model: CustomUser

admin.site.register(CustomUser, CustomUserAdmin)