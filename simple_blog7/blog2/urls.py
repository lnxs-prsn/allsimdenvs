from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('post/<int:pk>/update', views.post_update, name='post_update'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/create_new', views.post_create, name='post_create'),
    path('', views.post_list, name='post_list')
    path('login/', LoginView.as_view(template_name='login.html'), name='login')
    path()
]