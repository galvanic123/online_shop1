from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CatalogHomeView, CatalogContactsView, CatalogDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", CatalogHomeView.as_view(), name="home"),
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path("product_detail/<int:pk>/", CatalogDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]

# urlpatterns = [
#     path("home/", views.home, name="home"),
#     path("contacts/", views.contacts, name="contacts"),
#     path("product_detail/<int:product_id>", views.product_detail, name="product_detail"),
#     path("product_list/", views.product_list, name="product_list"),
# ]
