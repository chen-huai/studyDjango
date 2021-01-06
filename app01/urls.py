from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book),
    path('search_book/', views.search_book),
    path('exclude_book/', views.exclude_book),
    path('reverse_book/', views.reverse_book),
]