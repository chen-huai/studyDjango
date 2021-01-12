from django.contrib import admin

# Register your models here.
from django.contrib import admin
from moreTable.models import *




class PublishAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'city', 'email')
    search_fields = ('name',)
    def __unicode__(self):              # __str__ on Python 3
        return self.name

admin.site.register(Publish,PublishAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'price', 'publish_name')
    # fk_fields 设置显示外键字段
    def publish_name(self, obj):
        return obj.publish.name
    fk_fields = ('name',)
    search_fields = ('title',)

admin.site.register(Book,BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'age', 'au_detail_id')
    search_fields = ('name',)

admin.site.register(Author,AuthorAdmin)

class AuthorDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender','tel', 'addr','birthday')

admin.site.register(AuthorDetail,AuthorDetailAdmin)