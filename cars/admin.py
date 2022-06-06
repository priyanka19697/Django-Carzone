from django.contrib import admin
from django.utils.html import format_html
from cars.models import Car

# Register your models here.

class CarsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Photo'
    list_display = ('car_title', 'thumbnail', 'model', 'year', 'body_style', 'fuel_type', 'is_featured', 'state')
    list_display_links = ('car_title', 'thumbnail')
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'state', 'model', 'body_style', 'fuel_type')
    list_filter = ('state', 'year','fuel_type')
admin.site.register(Car, CarsAdmin)
