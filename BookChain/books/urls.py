from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search-book/', views.search_book, name='search_book'),
    path('success/', views.success, name='success'),
]
