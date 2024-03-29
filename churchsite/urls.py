from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("swbc.urls")),
    path("books/", include("bookstore.urls")),
    path("devotionals/", include("devotionals.urls")),
    path("sermons/", include("sermons.urls")),
    path("newsevents/", include("newsevents.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
