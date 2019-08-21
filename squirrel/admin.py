from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Article
from .forms import SquirrelUserCreationForm, SquirrelUserChangeForm
from .models import SquirrelUser


class SquirrelUserAdmin(UserAdmin):
    add_form = SquirrelUserCreationForm
    form = SquirrelUserChangeForm
    model = SquirrelUser
    list_display = ['email', 'username',]

admin.site.register(SquirrelUser, SquirrelUserAdmin)
admin.site.register(Article)
