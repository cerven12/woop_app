from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


from .models import CustomUser

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password',)

class CustomUserAdmin(UserAdmin):
    # Admin site display, each taple of index 0 is label.
    fieldsets = (
            (_('Login'), {'fields': ('email', 'username', 'password',)}),
        (_('Personal info'), {'fields': ()}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    # User create Admin site
    add_fieldsets = (
            (_('Create User'), {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'username', 'is_staff','user_id',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    search_fields = ('email', 'username','user_id')
    ordering = ('email',)
admin.site.register(CustomUser, CustomUserAdmin)

