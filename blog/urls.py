
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)