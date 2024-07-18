from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('books/', views.home, name='book_list'),
    path('books/<str:isbn>/', views.book_detail, name='book_detail'),
    path('books/<str:isbn>/add_review/', views.add_review, name='add_review'),
    path('register/', views.register_user, name='register'),
    path('login_user/', views.login_view, name='login'),
    path('logout_user/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<str:isbn>/edit/', views.edit_book, name='edit_book'),
    path('books/<str:isbn>/delete/', views.delete_book, name='delete_book'),
]