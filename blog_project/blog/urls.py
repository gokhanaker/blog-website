from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('signup/validate/', views.validateSignup, name = 'validateSignup'),
    path('login/', views.login, name = 'login'),
    path('login/validate/', views.validateLogin, name = 'validateLogin'),
    path('logout/', views.logout, name = 'logout'),
    path('', views.postList, name='postList'),
    path('post/<int:post_id>/', views.postDetail, name='postDetail'),
    path('post/new/', views.newPost, name= 'newPost'),
    path('post/new/publish/', views.publishPost, name = 'publishPost'),
    path('post/edit/<int:post_id>/', views.editPost, name = 'editPost'),
    path('post/edit/<int:post_id>/update/', views.updatingEditedPost, name = 'updatingEditedPost'),
    path('post/delete/<int:post_id>/', views.deletePost, name = 'deletePost'),
    path('post/like/<int:post_id>/', views.likePost, name = 'likePost'),
    path('post/<int:post_id>/add/comment/', views.addComment, name = 'addComment'),
    path('post/<int:post_id>/add/comment/publish/', views.publishComment, name = 'publishComment'),
    path('post/<int:post_id>/edit/comment/<int:comment_id>/', views.editComment, name = 'editComment'),
    path('post/<int:post_id>/edit/comment/<int:comment_id>/update/', views.updateEditedComment, name = 'updateEditedComment'),
    path('post/<int:post_id>/delete/comment/<int:comment_id>/', views.deleteComment, name = 'deleteComment')
]
