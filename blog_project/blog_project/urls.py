from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



handler404 = 'blog.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    # there is only 1 django app in this project
    path('', include('blog.urls'))
]

# adding a special URL debugging url to serve our media files locally
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
