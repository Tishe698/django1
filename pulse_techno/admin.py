from django.contrib import admin

from .models import Image,Image2,Image3


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image1', 'description', 'is_published',)
    list_display_links = ('is_published',)
    fields = ('image1', 'description')


admin.site.register(Image, ImageAdmin)
admin.site.register(Image2, ImageAdmin)
admin.site.register(Image3, ImageAdmin)
