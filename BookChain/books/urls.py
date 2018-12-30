from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('search-book/', views.search_book, name='search_book'),
    path('success/', views.success, name='success'),
    path('user/profile', views.user_profile, name='profile'),
]
