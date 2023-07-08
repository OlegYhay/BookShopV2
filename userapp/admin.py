from django.contrib import admin

# Register your models here.

from .models import CustomUser
from .forms import UserChangeCustomForms, UserCreationCustomForms

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationCustomForms
    form = UserChangeCustomForms
    list_display = ['username', 'email']
