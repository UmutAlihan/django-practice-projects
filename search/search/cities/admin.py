from django.contrib import admin

from .models import City

# Register your models here.

class CityAdmin(admin.ModelAdmin):
    last_display = ("name", "state",)


admin.site.register(City, CityAdmin)
