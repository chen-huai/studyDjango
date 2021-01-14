from django.contrib import admin
from region.models import *
# Register your models here.
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id','zoneName')
    # search_fields = ('zoneName',)

admin.site.register(Zone, ZoneAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','departmentName')
    search_fields = ('name',)

admin.site.register(Department, DepartmentAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id','room','area','place')
    search_fields = ('room',)

admin.site.register(Place, PlaceAdmin)
