from django.contrib import admin

# Register your models here.
from .models import Salon, Mutfak, KucukOda, YatakOda, Tuvalet


class SalonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

class MutfakAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

class KucukOdaAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

class YatakOdaAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

class TuvaletAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


admin.site.register(Salon, SalonAdmin)
admin.site.register(Mutfak, MutfakAdmin)
admin.site.register(KucukOda, KucukOdaAdmin)
admin.site.register(YatakOda, YatakOdaAdmin)
admin.site.register(Tuvalet, TuvaletAdmin)
