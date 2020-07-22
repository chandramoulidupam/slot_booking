# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userapp.models.models import User

# admin.site.register(User, UserAdmin)
admin.site.register(User)
# your django admin
