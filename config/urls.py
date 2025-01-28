from django.contrib import admin
from django.urls import path, include
from catalog.views import home, contacts

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', home),
    path("catalog/", include("catalog.urls", namespace='catalog')),
]
