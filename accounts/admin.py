from django.contrib import admin

from accounts.models import Profile, Address
# Register your models here.

admin.site.register(Profile)
admin.site.register(Address)

