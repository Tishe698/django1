from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image1', 'image2', 'description','is_published',)
    list_display_links = ('is_published',)
    fields = ('image1', 'image2', 'description')


admin.site.register(Image, ImageAdmin)
