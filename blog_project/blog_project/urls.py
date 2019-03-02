from django.contrib import admin
from django.urls import path, include

handler404 = 'blog.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    # there is only 1 django app in this project
    path('', include('blog.urls')),
]
