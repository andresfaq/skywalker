# from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# admin.site.unregister(User)
# admin.site.register(User, models.ProfileUser)
# admin.site.register(models.ProfileUser)

# admin.site.register(models.Employee)
# admin.site.register(models.Client)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + \
            ('address', 'date_of_birth', 'cellphone', 'dni', 'phone',)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields #+ ('address', 'date_of_birth', 'cellphone', 'dni', 'phone',)

class CustomUserAdmin(UserAdmin):  
    add_form = CustomUserCreationForm   

admin.site.register(CustomUser, UserAdmin)