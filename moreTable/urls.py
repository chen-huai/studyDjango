from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('add_book/', views.add_book),
    re_path(r'^addBToA/(?i)',views.add_book_author)
]