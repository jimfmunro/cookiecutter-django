from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as djUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

class UserAdmin(djUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password', 'last_login', 'date_joined',)}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_superuser', 'is_active')
    ordering = ('email',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )

    form = UserChangeForm
    add_form = UserCreationForm

admin.site.register(User, UserAdmin)
