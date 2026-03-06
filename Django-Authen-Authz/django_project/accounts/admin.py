# >---------------------------------------<
# (Django Admin Configuration) -----------<
# >---------------------------------------<

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from accounts.models import User
from accounts.forms import CreateUserForm, ChangeUserForm


@admin.register(User)
class UserAdmin(BaseAdmin):
    # Custom admin interface for User model
    # Forms for editing and creating users
    form = ChangeUserForm
    add_form = CreateUserForm

    # Display configuration
    list_display = ["email", "first_name", "last_name", "created_at", "is_superuser"]
    list_filter = ["is_superuser"]
    
    # Edit form layout
    fieldsets = [
        (None, {"fields": ["email", "first_name", "last_name", "is_superuser"]}),
    ]
    
    # Add form layout
    add_fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_superuser",
                ]
            },
        ),
    ]
    
    # Search and ordering
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ()


# Remove default Group model from admin
admin.site.unregister(Group)
