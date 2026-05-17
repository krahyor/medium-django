from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from medium.models.users import User
from medium.models.blogs import Blog

admin.site.register(User, UserAdmin)
admin.site.register(Blog)
