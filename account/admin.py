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
        fields = ('email',)

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        # index 0 show change form for field.
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('username',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'username',  'is_staff','user_id',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    search_fields = ('email', 'username','user_id')
    ordering = ('email',)
admin.site.register(CustomUser, CustomUserAdmin)

