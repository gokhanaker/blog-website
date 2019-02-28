from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.postList, name='postList'),
    # path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.postDetail, name='postDetail'),
    path('post/new/', views.newPost, name= 'newPost'),
    path('post/new/publish/', views.publishPost, name = 'publishPost'),
    path('post/edit/<int:post_id>/', views.editPost, name = 'editPost'),
    path('post/edit/<int:post_id>/update/', views.updatingEditedPost, name = 'updatingEditedPost'),
    path('post/delete/<int:post_id>/', views.deletePost, name = 'deletePost'),
    path('post/like/<int:post_id>/', views.likePost, name = 'likePost')
]
