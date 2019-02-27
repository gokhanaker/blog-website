from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.postList, name='postList'),
    # path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.postDetail, name='postDetail'),
    path('post/new/', views.newPost, name= 'newPost'),
    path('post/new/publish/', views.publishPost, name = 'publishPost')
]
