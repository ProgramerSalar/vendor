from django.contrib import admin
from .models import  User , UserProfile
from django.contrib.auth.admin import UserAdmin 


# Register your models here.
class CustomUserAdmin(UserAdmin):
    
    # show the that in panel
    list_display = ('email' , 'first_name' , 'last_name' , 'username', 'role' , 'is_active')
    ordering = ('-date_joined',)
    
    # password encrypt
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register( User , CustomUserAdmin)
admin.site.register(UserProfile)