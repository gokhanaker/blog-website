from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.postList, name='postList'),
    # path('about/', views.about, name='about'),
    path('blog/<int:post_id>/', views.postDetail, name='postDetail'),
]
