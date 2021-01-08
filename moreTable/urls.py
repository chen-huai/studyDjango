from django.contrib import admin
from django.urls import path,re_path
from . import views,formOperate

urlpatterns = [
    path('add_book/', views.add_book),
    re_path(r'^addBToA/(?i)',views.add_book_author),
    re_path(r'^add_b2a/(?i)',views.add_b2a),
    re_path(r'^search1/(?i)',views.search1),
    re_path(r'^search2/(?i)',views.search2),
    re_path(r'^search3/(?i)',views.search3),
    re_path(r'^add_emp/(?i)',formOperate.add_emp),
]