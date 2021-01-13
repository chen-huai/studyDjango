# Register your models here.
from django.contrib import admin
from moreTable.models import *

from django.contrib import admin
admin.site.site_header = "后台管理"
admin.site.site_title = '后台管理'

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'price', 'publish_name')

    def publish_name(self, obj):
        return obj.publish.name
    # 设置排序字段，负号表示降序排序
    ordering = ('id',)
    # 列表顶部，设置为False不在顶部显示，默认为True。
    actions_on_top = True
    # fk_fields 设置显示外键字段
    fk_fields = ('publish_name',)
    search_fields = ('title',)
    # list_filter = 设置一个过滤器
    # list_filter = ("publish_name",)
    # 分页显示
    list_per_page = 20
    # 分页控件，使用django默认控件
    # paginator = Paginator

admin.site.register(Book,BookAdmin)

class PublishAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'city', 'email')
    search_fields = ('name',)
    # def __unicode__(self):              # __str__ on Python 3
    #     return self.name

admin.site.register(Publish,PublishAdmin)




class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'age', 'au_detail_id')
    search_fields = ('name',)

admin.site.register(Author,AuthorAdmin)

class AuthorDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender','tel', 'addr','birthday')

admin.site.register(AuthorDetail,AuthorDetailAdmin)