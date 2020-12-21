from django.urls import include, re_path
# from django.conf.urls import url
from . import views,testdb,search,search2
urlpatterns = [
    re_path(r'^$', views.hello),
    re_path(r'runoob/', views.runoob),
    re_path(r'img/', views.runoob),
    re_path(r'baby/', views.baby),
    re_path(r'add/', testdb.add),
    re_path(r'getData/', testdb.getData),
    re_path(r'update/', testdb.update),
    re_path(r'delete/', testdb.delete),
    re_path(r'^search-form/$', search.search_form),
    re_path(r'^search/$', search.search),
    re_path(r'^search-post/$', search2.search_post),
    # url(r'^search-form/$', search.search_form),
    # url(r'^search/$', search.search),
    # re_path(r'^index/$', views.index, name='index'),
    # re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
    # re_path(r'^weblog/', include('blog.urls')),
]