from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','age','gender', 'address','state_of_origin', 'phone_no')

    def user_info(self, object):
        return object.address

admin.site.register(Profile, ProfileAdmin)