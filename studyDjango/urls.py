from django.urls import include, re_path
from . import views,testdb
urlpatterns = [
    re_path(r'^$', views.hello),
    re_path(r'runoob/', views.runoob),
    re_path(r'img/', views.runoob),
    re_path(r'baby/', views.baby),
    re_path(r'testdb/', testdb.testdb),
    re_path(r'getData/', testdb.getData),
    # re_path(r'^index/$', views.index, name='index'),
    # re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
    # re_path(r'^weblog/', include('blog.urls')),

]