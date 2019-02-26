from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # there is only 1 django app in this project
    path('', include('blog.urls')),
    # path('login/', views.loginView, name = login),
    # path('logout/', views.logoutView, name = logout)
]
