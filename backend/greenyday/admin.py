from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Menu, Review

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['photo_tag', 'name', 'caption']
    list_display_links = ['name']

    def photo_tag(self, menu):
        return mark_safe(f"<img src={menu.photo.url} style='width: 100px;' />")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass