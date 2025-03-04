from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDeleteView, BlogDetailView, BlogUpdateView, CatalogContactsView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/paper_list/', BlogListView.as_view(), name='paper_list'),
    path('blog/paper_detail/<int:pk>/', BlogDetailView.as_view(), name='paper_detail'),
    path('blog/paper_form/', BlogCreateView.as_view(), name='paper_create'),
    path('blog/paper_list/<int:pk>/update/', BlogUpdateView.as_view(), name='paper_update'),
    path('blog/paper_list/<int:pk>/delete/', BlogDeleteView.as_view(), name='paper_delete'),
    path("blog/contacts/", CatalogContactsView.as_view(), name="contacts"),
]
