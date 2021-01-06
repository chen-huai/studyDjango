from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app01.models import Book



class BookAdmin(admin.ModelAdmin):
    list_display = ('title','pk', 'price', 'publish')
    search_fields = ('title',)

admin.site.register(Book,BookAdmin)