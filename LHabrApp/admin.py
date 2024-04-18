from django.contrib import admin
from .models import CustomUser, Post


class Users(admin.ModelAdmin):
    list_display = ('email', 'username')


admin.site.register(CustomUser, Users)


class Users(admin.ModelAdmin):
    list_display = ('title', 'date_posted')


admin.site.register(Post)
