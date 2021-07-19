from django.contrib import admin

from .models import Banner, User


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_data', 'action', 'status')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'secret', 'username', 'image_data')
