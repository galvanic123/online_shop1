from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from catalog.views import start_home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", start_home, name="start_home"),
    path("catalog/home/", include("catalog.urls", namespace="catalog")),
    path("blog/paper_list", include("blog.urls", namespace="blog")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
