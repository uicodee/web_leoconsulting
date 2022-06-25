from django.contrib import admin

from .models import Region, User


@admin.register(Region)
class RegionsAdmin(admin.ModelAdmin):
    list_display = ("id", "region_name",)
    list_editable = ("region_name",)
    list_display_links = ("id",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "name")
    list_display_links = ("id", "user_id", "name")
