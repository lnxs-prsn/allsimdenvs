from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int_pk/edit/', views.PostUpdateViews.as_view(), name='post_edit'),
    path('post/<int_pk>/delete/', views.PostDeleteViews.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', views.CommentCreateViews.as_view(), name='add_comment'),
]