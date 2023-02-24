from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User
fields = list(UserAdmin.fieldsets)
fields.insert(2,('Other Info', {'fields': ('designation',)}))
UserAdmin.fieldsets = tuple(fields)
admin.site.register(User,UserAdmin)

#user admin will display the custom user model in admin panel