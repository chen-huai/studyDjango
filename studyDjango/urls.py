# from django.conf.urls import url
from django.contrib import admin
from django.urls import include, re_path,path
from . import views,testdb,search,search2
urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^admin/', admin.site.urls),
    re_path(r'^$(?i)', views.hello),
    re_path(r'runoob/$(?i)', views.runoob),
    re_path(r'img/$(?i)', views.runoob),
    re_path(r'baby/$(?i)', views.baby),
    re_path(r'add/$(?i)', testdb.add),
    re_path(r'getData/$(?i)', testdb.getData),
    re_path(r'update/$(?i)', testdb.update),
    re_path(r'delete/$(?i)', testdb.delete),
    re_path(r'^search-form/$(?i)', search.search_form),
    re_path(r'^search/$(?i)', search.search),
    re_path(r'^search-post/$(?i)', search2.search_post),
    re_path(r'^getMethod/$(?i)', views.getMethod),
    re_path(r'^postMethod/$(?i)', views.postMethod),
    re_path(r'^bodyMethod/$(?i)', views.bodyMethod),
    re_path(r'^pathMethod/$(?i)', views.pathMethod),
    re_path(r'^httpRes/$(?i)', views.httpRes),
    re_path(r'^renderMethod/$(?i)', views.renderMethod),
    path('redirectMethod/', views.redirectMethod),
    # url(r'^search-form/$(?i)', search.search_form),
    # url(r'^search/$(?i)', search.search),
    # re_path(r'^index/$(?i)', views.index, name='index'),
    # re_path(r'^bio/(?P<username>\w+)/$(?i)', views.bio, name='bio'),
    re_path(r'^app01/', include('app01.urls')),
]